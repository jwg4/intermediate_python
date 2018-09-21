def xs128p(state0, state1):
    # save states to temp variables for operating
    s1 = state0 & ((1<<64)-1)
    s0 = state1 & ((1<<64)-1)
    
    # generate next state1
    s1 ^= (s1 << 23) & ((1<<64)-1)
    s1 ^= (s1 >> 17) & ((1<<64)-1)
    s1 ^= s0 & ((1<<64)-1)
    s1 ^= (s0 >> 26) & ((1<<64)-1)
    
    # update state0
    state0 = state1 & ((1<<64)-1)
    # update state1
    state1 = s1 & ((1<<64)-1)
    
    # return updated state and the pseudo random number
    generated = (state0 + state1) & ((1<<64)-1)
    return state0, state1, generated
