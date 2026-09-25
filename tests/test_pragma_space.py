from hlsdse.pragma_space import generate_cartesian
def test_cartesian():
    cs=list(generate_cartesian({'pipeline':['on','off'],'unroll':[1,2]},'b'))
    assert len(cs)==4
