import itertools

def comb_no_dup(in_lst, n=3):
    """Create combinations with size n..2 with no repeated pairs between combinations."""
    done_pairs = []
    for size in range(n,1,-1):
        for comb in itertools.combinations(in_lst, size):
            pairs = list(itertools.combinations(comb,2))
            if all(i not in done_pairs for i in pairs):
                done_pairs += pairs
                yield comb
        
