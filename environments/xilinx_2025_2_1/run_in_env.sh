#!/usr/bin/env bash
# Project-scoped launcher for the AMD-Xilinx 2025.2.1 toolchain (Vivado, Vitis, Vitis HLS).
#
# Usage (from the HLS_DSE project root):
#   environments/xilinx_2025_2_1/run_in_env.sh <command> [args...]
#   environments/xilinx_2025_2_1/run_in_env.sh --check
#
# Re-executes itself under `env -i` so the caller's interactive shell (PATH, pyenv/venv
# shims, ISE/2023.2 variables, ~/.local/bin wrappers) cannot leak in, sources the vendor
# settings64.sh, prepends the project-local vitis_hls shim, and refuses to run if any
# selected tool resolves outside the 2025.2.1 release tree.
# It does not modify shell startup files, the Xilinx installation, or license configuration.
set -euo pipefail

XILINX_RELEASE=2025.2.1
XILINX_ROOT=/mnt/data/Apps/2025.2.1
VENDOR_SETTINGS="$XILINX_ROOT/Vivado/settings64.sh"
VENDOR_SETTINGS_SHA256=c53e2d30fe4b09067fe6894d11a9fc11fedda82d4fb1f506878a67a6d7aab3bb
BASE_PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# The only caller variables passed through env -i. Values are never printed.
LICENSE_ALLOWLIST=(XILINXD_LICENSE_FILE LM_LICENSE_FILE)

ENV_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ "${HLSDSE_XILINX_ENV:-}" != "$XILINX_RELEASE" ]]; then
    license_env=()
    for var in "${LICENSE_ALLOWLIST[@]}"; do
        [[ -n "${!var:-}" ]] && license_env+=("$var=${!var}")
    done
    exec env -i \
        HOME="$HOME" USER="${USER:-$(id -un)}" LOGNAME="${LOGNAME:-$(id -un)}" \
        LANG="${LANG:-C.UTF-8}" TERM="${TERM:-dumb}" \
        PATH="$BASE_PATH" HLSDSE_XILINX_ENV="$XILINX_RELEASE" \
        "${license_env[@]}" \
        bash --noprofile --norc "${BASH_SOURCE[0]}" "$@"
fi

die() { echo "HLSDSE_ENV_ERROR: $*" >&2; exit 3; }

[[ -r "$VENDOR_SETTINGS" ]] || die "vendor settings not found: $VENDOR_SETTINGS"
actual_sha="$(sha256sum "$VENDOR_SETTINGS" | cut -d' ' -f1)"
[[ "$actual_sha" == "$VENDOR_SETTINGS_SHA256" ]] || die "vendor settings hash mismatch: $actual_sha"
grep -qx "XILINX_VERSION_DEFAULT=$XILINX_RELEASE" "$XILINX_ROOT/data/version.sh" \
    || die "release marker $XILINX_ROOT/data/version.sh does not declare $XILINX_RELEASE"

# shellcheck disable=SC1090
source "$VENDOR_SETTINGS" >/dev/null
export PATH="$ENV_DIR/bin:$PATH"
export PYTHONDONTWRITEBYTECODE=1

for var in XILINX_VIVADO XILINX_VITIS XILINX_HLS; do
    [[ "${!var:-}" == "$XILINX_ROOT"/* ]] || die "$var=${!var:-<unset>} is not inside $XILINX_ROOT"
done

IFS=: read -ra path_entries <<< "$PATH"
for entry in "${path_entries[@]}"; do
    case "$entry" in
        *2023.2*|*Vitis_HLS*|/tools/Xilinx*|/opt/Xilinx*|*/.local/bin|*pyenv*|*/.venvs/*)
            die "forbidden PATH entry: $entry" ;;
    esac
done

for tool in vivado vitis vitis_hls vitis-run v++; do
    exe="$(command -v "$tool")" || die "$tool not found"
    real="$(readlink -f "$exe")"
    [[ "$real" == "$XILINX_ROOT"/* || "$real" == "$ENV_DIR/bin/$tool" ]] \
        || die "$tool resolves outside the $XILINX_RELEASE environment: $real"
done

if [[ "${1:-}" == "--check" ]]; then
    echo "HLSDSE_XILINX_ENV=$XILINX_RELEASE"
    echo "VENDOR_SETTINGS=$VENDOR_SETTINGS sha256=$actual_sha"
    for var in XILINX_VIVADO XILINX_VITIS XILINX_HLS; do echo "$var=${!var}"; done
    for var in "${LICENSE_ALLOWLIST[@]}"; do echo "$var=$([[ -n "${!var:-}" ]] && echo '<SET>' || echo '<UNSET>')"; done
    for tool in vivado vitis vitis_hls vitis-run v++ python3; do
        exe="$(command -v "$tool")"; echo "$tool=$exe -> $(readlink -f "$exe")"
    done
    echo "PATH=$PATH"
    exit 0
fi

[[ $# -gt 0 ]] || { echo "usage: $0 --check | <command> [args...]" >&2; exit 2; }
exec "$@"
