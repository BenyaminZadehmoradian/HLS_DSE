# Literature Normalization Policy

External results are classified as:

1. `LITERATURE_REPORTED`: copied/paraphrased from a source with citation.
2. `REPRODUCED`: our execution of the published method/artifact.
3. `OUR_MEASURED`: measurement produced by our current method/baseline implementation.
4. `REFERENCE_ORACLE`: exhaustive or otherwise explicitly defended reference set.

A direct numerical comparison requires alignment of:
- benchmark/source revision
- top function and input set
- pragma/design space
- device/board/package/speed grade
- HLS/RTL/implementation tool versions
- clock constraints
- correctness criteria
- objective/constraint definitions
- evaluation stage
- search/evaluation budget
- repetition/statistical protocol

If any material field differs, the comparison is labeled `INDIRECT_ONLY` unless a controlled re-evaluation is performed.
