#### 要復習問題

1,4,10,13,14,20,21,23,26,27,34
40,43,44,45,46,51,52,53,59,61,63,66,69,70,72,73,74

#### 回答

1. a, b, c fxとは　✗ c, e, f
- ＋や-などの算術演算子を含む式の前後　→　暗黙変換で数値への変換が試みられる
- MON⇔MONTH、RR⇔RRRRは自動的に置き換えた変換がされる
- DDは形式に合わない場合自動的に先頭ゼロ補完がされた
- 区切り記号 . - , : の暗黙変換は可能
2. a
3. b
4. a ✗ a, d
5. a
6. c
7. b, e
8. c
9. a, d, e
10. a? ✗ c
- DISTINCTはSELECT句の選択列の最初に１回だけ指定
11. c 
12. c
13. c?
- SELECT句で定義した列別名→同じSELECT文内で列別名を参照したり、式で使用したりできない
14. c, e eの書き方 ✗ b, c
- NULLはデフォルトでは最大の値
- NULLS FIRSTだけでも最初にくる（このときNULL以外は順不同）
15. c, e
16. a, d
17. a, d
18. b, c
19. d
20. b ✗ d
- ミス！bはDESCがない
21. a?
- ORDER BYに計算式の指定は可能
22. a
23. c _は0文字以上？ ✗ d
- %は任意の1文字, _は任意の0文字
24. a, b, d
25. b
26. a, d ✗ a, c
- DATE型の日付は内部的には数値形式で格納される
27. a INSTR当てはまらないとき0が返される？
- INSTR(文字列1, 文字列2, m, n)→文字列2がないとき0が返される
28. a, b, d
29. b
30. a 
31. a, b
32. a, c
33. b
34. c, f ✗ b, c
- 「Gと.」や「,とD」という組み合わせは使用できない
- 0を指定すると先行0や小数点以下後続0も表示される
- 9を指定すると先行0は表示されないが後続0は表示される
- fmで先行0後続0の表示・不表示の指定が可能
- 書式V：Vに続くn個の個数について、10^nが表示される
35. d

------

36min ✗ 8コ

------

36. c
37. d
38. b, c, d, e
39. e
40. b?
- FROM句で表別名→SELECT文全体で表名の代わりに表別名を指定しないとエラー
41. b
- LISSTAG(連結して表示する列名[, デミリタ]) WITHIN GROUP(ORDER BY ソート列名[, DESC])
- デミリタは省略可能
42. d
43. b?e?　✗ a
- CASE式：戻り値にNULL可能
- グループ関数の中にCASE式を指定できる
- 検索CASE式：複数の条件を指定できる
44. f　✗ a
- SELECT句でグループ関数と一緒に指定できる列はgroup byで指定した列だけ
45. c, d? d「SELECT句にグループ関数を指定している場合」? ✗ c,d
- 44参照
46. ? ✗ c, d
- ネストしたグループ関数を使用する　→　SELECT句にはネストしたグループ関数だけを指定する必要がある
47. d
48. a, d
49. c
50. a
51. d (c?)
- SQL1999構文とOracle構文にパフォーマンスの違いはない
52. b?
53. ✗ b, c
- 結合方法の問題
54. d, f
55. a, e
56. b
57. d
58. a
59. b, c, f? 
- 明示的なCOMMIT文とROLLBACK文の他にDDL文の実行でもトランザクションは完結する
- DML  
    SELECT, INSERT, UPDATE, DELETE, MERGE
- DDL  
    CREATE, ALTER, DROP, RENAME, TRUNCATE, COMMENT
60. c
61. a?
- INSERT文の表名の代わりに副問合せ、VALUESに副問合せを指定できる
- 副問合せの結果を列名には指定できない
62. a
63. ? ✗d
- PRIMARY KEY制約は表作成時、作成後に定義できる。
- 表作成後にPRIMARY KEY制約を追加する場合には、すでに登録されているデータにNULL値、重複値があってはならない
64. c
65. d
- CHECK　疑似列の参照、SYSDATE関数の呼び出しはできない
- DEFAULTに　疑似列（12c~）、SYSDATEはOK
66. c?
- CLOB　最大4G、列の定義時にサイズを指定するとエラー
67. c, e
68. b
69. c?, d
- NOT NULL制約と複合列の制約以外はすべて、列レベルと表レベルで定義できる
70. e, f ✗ d, f
- ALTER TABLE 表名 SET UNUSED (列名[, 列名]);　ALTER TABLE 表名 SET UNUSED COLUMN(列名);
- ALTER TABLE 表名 DROP UNUSED COLUMNS;
- 制約、索引は削除／ビューは自動で修正されない／シノニムの再作成は必要ない
71. c
- ALTER TABLE 表名 MODIFY (列名[, データ型])
72. ? ✗ b, d
- 別の表から参照されている主キー  
    - 外部キー制約を削除
    - ALTER TABLE 表名 DROP 文でCASCADE CONSTRAINTS句を指定
73. a, c, d(b?)
- LONG型  
    UNIQUE制約、GROUP BY、ORDER BY使えない
74. b, c ✗a, c
- ALTERはDDL
75. d

------

60min ✗8