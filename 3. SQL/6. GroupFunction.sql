
/*
SELECT文に指定する句の順序
1.SELECT句
2.FROM句
3.WHERE句
4.GROUP BY句
5.HAVING句
6.ORDER BY句
*/


-- （評価順）　FROM句→WHERE句→GROUP BY句→HAVING句→SELECT句→ORDER BY句


/* GROUP BYのルール */
-- GROUP BY句に列別名を指定できません  
-- GROUP BY句を指定したSELECT文のSELECT句には、GROUP BY句で指定した列、もしくはグループ関数のみ指定できます  
-- GROUP BY句とORDER BY句を併用する場合、ORDER BY句にはGROUP BY句で指定した列、もしくはグループ関数のみ指定できます  


LISTAGG(measure_expr, delimiter) WITHIN GROUP(ORDER BY (order_by clause))

-- measure_exprには、任意の式を指定できます。メジャー列のNULL値は無視されます。
-- delimiter_exprには、メジャー値の区切りに使用する文字列を指定します。この句はオプションであり、デフォルトはNULLです。
-- order_by_clauseには、結合した値を戻す順序を指定します。このファンクションが決定的となるのは、ORDER BYの列リストの順序が一意になった場合のみです。


-- グループ関数を使用できるのは、SELECT句、ORDER BY句、HAVING句のみ

-- *：NULL含む全て
-- ALL：NULL含まない全て
-- DISTINCT：NULL・重複を含まない全て