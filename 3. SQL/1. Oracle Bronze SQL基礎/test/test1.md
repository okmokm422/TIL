#### 要復習問題

2,3,5,9,10,11,13,14,16,17,18,20,24,25,28,29,31,33,34,35
41,48,51,52,58,60,62,63,65,67,68,71,72,73,75

#### 回答

1. d
2. d ✗   
- TO_NUMBERで計算後、TO_CHARで文字列形式に
3. c　✗  
- 第１正規形：主キーに対して複数回現れる列がない
- 第２正規形：すべての属性が主キーに依存している（部分関数従属性がない）
- 第３正規形：主キーではない属性に依存する属性がない（推移関数従属性がない）
4. c
5. a?, c
6. b
7. b
8. a, b
9. a, b
- 文字連結演算子 ||
10. b
- COUNTはグループ関数のため、HAVINGに指定
11. c　✗ミス
12. b
13. d
- OFFSET句/FETCH句はORDER BY句の後に指定
- OFFSET offset {ROW | ROWS}
  FETCH {FIRST | NEXT}
        {row_count | percent PERCENT}
        {ROW | ROWS}
        {ONLY | WITH TIES}
14. a,? d, f　✗ a, e, f
- セーブポイントはROLLBACKに対してのみ使用できる
- セーブポイントは論理的なものであるため、セーブポイント一覧は表示できない
- DMLに対してのみ使用できる
15. a
16. d FETCHの復習！ ✗ b
- FETCHに NEXT | FIRSTの指定は必須 
17. b
- MONとMONTHの暗黙変換は可能
18. ?　✗ b, e
- NULLIF()の中身がNULL→結果NULL
- NULLIFの第一引数にリテラルNULLは指定できない
19. a, d
20. a MONTHS_BETWEENの小さい方は右！
21. c
22. c, d, e
23. a(LENGTH), d(NULLIF)
24. a, e(MONTHS_BETWEEN?)
- NVL, NVL2→最初の引数の型に暗黙変換できないとエラー
25. b, c スペースは認識されない?　✗ a, b
- TO_DATE：書式指定しておらず、デフォルトの書式の形式とも一致しないとエラー
26. c
27. a, d
28. e ✗ b
- UPDATEのSET句でも副問合せを使用可
29. c ✗ b
- BETWEEN D AND DならOK
- 条件に一致しない→エラーじゃなくてNULLで1件も返ってこない
30. d, e
31. a, d ✗ a, c
- 単純CASE式なので一致不一致の判定のみできる
- SUM 条件に一致：1　一致しない:0
- COUNT 条件に一致：任意の値　一致しない:NULL
- COUNT はデフォルトのALLとDISTINCTはNULLを除く、*は除かない
32. c
33. a ✗ d
34. a, c?, e　✗ a, b, e
35. b(?NULLの扱い), d　✗ c, d
- COUNT はデフォルトのALLとDISTINCTはNULLを除く、*は除かない

✗13

---40min---

36. d
37. c
38. a
39. a, b, d
40. d
41. c dはTRUNCの中身が数値？
- d 切り捨て最初に行ってから割ると端数が発生する
42. c
43. a
44. a
45. e
46. a, f
47. c
48. a, b(データグループ？), d
49. a
50. c
51. b?, d
52. a ✗ e
- 他の行の値と比較して取り出される要件は副問合せや結合を使用する必要がある。
53. a, b, c
54. c, e
55. d
56. d
57. b
58. b, c?, d
- WHERE句で複数の列の副問合せ→複数列の条件とする必要がある
59. c, d
60. c 副問合せとINSERT
- NOT NULL制約の列を指定せずINSERT→DEFAULT指定or指定しないとエラー
61. b
62. a 副問合せとUPDATE
- UPDATE文で表名の代わりに副問合せを利用できる→更新できるのは副問合せのSELECTで指定した列のみ
63. a　✗d
- VALUE句に指定する副問合せ  
  単一行副問合せ、単一列副問い合わせの必要がある
64. a, b
65. e?
- UNIQUE制約とPRIMARY KEY制約→索引が自動的に作成される
- NULL→NOT NULL制約・PRIMARY KEY制約がなければ入れられる
66. d
67. d
- 12cでは　NEXTVALやCURVALがデフォルト値として指定できる 
68. d ✗ a
- CREATE TABLE文ではOR REPLACEは使用できない
69. a
70. a
71. d?, f ✗ b, d
- 通常はUNUSEDマークをつけるとすぐに同じ名前の列を追加できるが、LONG型の列は物理的に削除しないと追加できない
72. c
- ADD COLUMN　→　ない
- 制約はDEFAULTオプションの後に書く
73. b, d?, e ✗ b, c, d
- DROP TABLEでは、索引は削除、依存オブジェクト（ビューやシノニム）は削除されない
74. b, d 
75. c, e?

✗　5