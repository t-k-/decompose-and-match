def remove_candiate(d, Q, C):
	for a in Q:
		if C_a is empty:
			return empty
		else
			C_a = C_a - {d} 
	return C

def decompose_and_match(Q, C):
	if Q is empty:
		return SUCC
	a = a_path_in(Q)
	new_Q = Q - a
	for a'' in C_a:
		new_C = remove_candiate(a'', new_Q, C)
		if new_C is empty:
			return FAIL
		if match(a, a'', new_Q, new_C) == SUCC:
			return SUCC
	return FAIL

def match(a, a'', Q, C):
	for b in Q:
		t = lcp(a, b)
		P = P U {t}
		Q_t = Q_t U {b}
	for t in P:
		for b in Q_t:
			for b'' in C_b:
				if t != lcp(a'',b''):
					C = remove_candiate(b'', Q_t, C)
					if C is empty:
						return FAIL
		if decompose_and_match(Q_t, C) == FAIL:
			return FAIL
	return SUCC
