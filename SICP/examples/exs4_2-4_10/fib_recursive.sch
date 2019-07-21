(display ((lambda (n)
	((lambda (fact)
		(fact fact n))
	(lambda (ft k)
		(if (< k 2)
			k
			(+ (ft ft (- k 1)) (ft ft (- k 2)))))))
	7))