# Real Winning Game with Py2048-Engine
Below is an example using the built-in tester of a winning game. This was done manually. Unlike many sites, this engine uses a flat 2/4 tile generation, not generation based on the values of surrounding tiles. This is how the game was originally designed, and makes the game harder as you progress.

<details>
<summary>Full Game Log (from Terminal with runTest()</summary>

```Python
[sam@Samarths-MacBook-Air] ~
❯ python3
Python 3.9.7 (default, Sep  3 2021, 04:31:11)
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from Py2048_Engine.Test import runTest
>>> runTest()
-	-	-	2
-	-	-	-
-	2	-	-
-	-	-	-
Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


2	-	-	-
-	2	-	-
2	-	-	-
-	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


2	-	-	-
2	-	-	-
2	-	-	2
-	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	-	-	2
2	2	-	-
-	-	-	-
-	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	2	-	-
4	-	-	-
-	-	-	-
-	2	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	-	-
-	-	-	-
-	2	-	-
-	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	-	-
-	2	-	-
-	-	-	-
-	-	2	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	2	-
-	2	-	-
-	-	-	2
-	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	2	2
-	2	-	-
-	-	2	-
-	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


8	4	4	-
2	-	-	-
2	-	2	-
-	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


8	8	-	-
2	-	-	-
4	2	-	-
-	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	8	-	-
2	2	-	-
4	-	-	-
-	-	2	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	-	-	-
4 	2	-	-
4 	-	-	-
2 	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	2	-	-
8 	-	-	-
2 	-	2	-
- 	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	2	-	2
8 	-	-	-
4 	-	-	-
- 	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	4	2	-
8 	-	-	-
4 	-	-	-
- 	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	4	2	-
8 	-	-	-
4 	-	-	-
- 	-	4	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	4	2	2
8 	-	-	-
4 	-	-	-
4 	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	4	2	2
8 	-	-	-
8 	-	-	-
- 	4	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	8	2	2
16	2	-	-
- 	-	-	-
- 	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	8	2	2
- 	2	-	2
- 	-	-	-
- 	-	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


2	32	8	4
-	- 	-	4
-	- 	-	-
-	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


2	32	8	8
-	- 	-	-
-	- 	-	-
-	- 	-	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


2	32	16	-
-	- 	- 	2
-	- 	- 	-
2	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	16	2
2	- 	- 	-
-	- 	- 	-
-	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	16	2
-	- 	- 	2
-	- 	- 	-
-	- 	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	16	4
-	2 	- 	2
-	- 	- 	-
-	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	16	4
-	- 	- 	4
-	- 	- 	-
-	- 	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	16	8
-	- 	2 	-
-	- 	- 	-
-	2 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	16	8
-	- 	- 	2
-	2 	- 	-
-	- 	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	16	8
-	2 	- 	4
-	- 	- 	-
-	2 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	16	8
-	4 	2 	4
-	- 	- 	-
-	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	32	16	8
4	2 	4 	-
-	- 	2 	-
-	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	16	8
-	4 	2 	4
-	2 	- 	2
-	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	32	16	8
4	2 	4 	-
4	- 	2 	-
-	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	16	8
-	4 	2 	4
2	- 	4 	2
-	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	32	16	8
4	2 	4 	-
2	4 	2 	-
-	- 	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	32	16	8
2	2 	4 	-
-	4 	4 	-
2	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	32	16	8
4	2 	8 	-
-	4 	- 	-
2	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	32	16	8
-	4 	2 	8
-	- 	2 	4
-	- 	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	32	16	16
2	4 	4 	4
-	- 	- 	2
-	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


8	32	32	-
2	8 	4 	2
2	- 	- 	-
-	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


8	64	-	-
2	8 	4	2
2	- 	-	-
2	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	64	4	2
4	8 	-	-
2	- 	-	-
-	- 	-	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


8	64	4	2
4	8 	-	4
2	- 	-	-
2	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	64	4	2
4	8 	-	4
4	- 	-	2
-	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	64	4	2
8	8 	2	4
-	- 	-	2
-	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	64	4	2
- 	8 	2	4
- 	- 	-	2
- 	- 	-	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	64	4	2
8 	2 	4	2
2 	- 	-	-
2 	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	64	8	4
8 	2 	-	-
4 	- 	-	2
- 	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	64	8	4
8 	2 	-	-
4 	2 	4	-
- 	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	64	8	4
8 	2 	-	-
4 	2 	4	-
- 	- 	-	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	64	8	4
8 	2 	-	4
4 	2 	4	-
2 	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	64	8	4
8 	2 	4	2
4 	2 	4	-
2 	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	64	8	4
8 	4 	8	2
4 	2 	-	-
2 	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	64	16	4
8 	4 	- 	2
4 	2 	2 	-
2 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	64	16	4
8 	4 	2 	-
4 	4 	- 	-
2 	- 	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	64	16	4
8 	4 	2 	2
8 	- 	- 	-
4 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	64	16	4
16	4 	2 	2
4 	- 	- 	2
- 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	16	4
4 	4 	2 	4
- 	2 	- 	-
- 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	16	4
8 	2 	4 	-
2 	- 	- 	2
- 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	16	4
8 	2 	4 	-
4 	- 	- 	-
2 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	64	16	4
- 	8 	2 	4
- 	- 	- 	4
- 	- 	2 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	16	4
8 	2 	4 	-
4 	2 	- 	-
4 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	16	4
8 	4 	4 	-
8 	2 	- 	-
- 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	16	4
16	4 	4 	-
- 	2 	2 	-
- 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	16	4
16	8 	- 	-
4 	2 	- 	-
- 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	64	16	4
- 	- 	16	8
- 	- 	4 	2
- 	- 	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	32	4
- 	- 	4 	8
2 	- 	- 	4
- 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	32	4
4 	8 	- 	-
2 	4 	- 	-
- 	- 	4 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	32	4
4 	8 	4 	-
2 	4 	2 	-
- 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	64	32	4
- 	4 	8 	4
2 	2 	4 	2
- 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	32	8
2 	4 	8 	2
2 	2 	4 	-
- 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	32	8
4 	4 	8 	2
- 	2 	4 	-
- 	- 	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	32	8
8 	8 	2 	-
2 	4 	- 	-
2 	- 	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	32	8
16	2 	- 	-
2 	4 	2 	-
4 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	32	8
16	2 	2 	-
2 	4 	- 	-
4 	2 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	32	8
16	4 	- 	2
2 	4 	- 	-
4 	2 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	32	8
16	8 	2 	2
2 	2 	- 	-
4 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	32	8
16	8 	4 	-
4 	2 	- 	-
4 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	64	32	8
- 	16	8 	4
- 	- 	4 	2
2 	- 	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	32	8
16	8 	4 	2
4 	2 	- 	-
2 	4 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	64	32	8
16	8 	4 	2
- 	2 	4 	2
- 	- 	2 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	32	8
16	8 	8 	4
- 	2 	2 	4
- 	- 	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	32	8
16	16	4 	2
4 	4 	- 	-
4 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	32	8
32	4 	2 	-
8 	- 	- 	-
4 	- 	4 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	64	32	8
8 	4 	2 	2
4 	- 	4 	-
- 	- 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	32	8	-
8  	4 	4	-
8  	- 	-	4
-  	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	32	8	-
8  	8 	2	-
8  	4 	-	-
-  	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	32	8	-
16 	8 	2	-
-  	4 	-	-
2  	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	128	32	8
2	16 	8 	2
-	-  	- 	4
-	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	32	8	-
2  	16	8	2
4  	- 	-	-
2  	- 	-	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	32	16	4
2  	16	- 	-
4  	- 	- 	-
2  	- 	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	32	16	4
2  	- 	2 	16
-  	- 	- 	4
-  	- 	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	32	16	4
4  	16	- 	-
4  	- 	- 	-
4  	- 	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	32	16	4
-  	- 	4 	16
-  	2 	- 	4
-  	- 	4 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	32	16	4
-  	2 	8 	16
-  	- 	- 	4
-  	4 	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	32	16	4
2  	8 	16	-
4  	2 	- 	-
4  	2 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	32	32	4
2  	8 	- 	-
8  	4 	- 	-
-  	2 	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	64	4	-
2  	8 	-	-
8  	4 	-	4
2  	- 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	64	4	4
2  	8 	-	-
8  	4 	-	-
2  	2 	-	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	128	64	8
-	-  	2 	8
-	-  	8 	4
-	2  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


-	128	64	16
-	2  	2 	8
-	-  	8 	-
4	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	128	64	16
-	-  	4 	8
-	-  	- 	8
-	-  	2 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


-	128	64	16
-	-  	4 	16
2	-  	2 	4
-	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


2	128	64	32
-	-  	4 	4
2	-  	2 	-
-	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	128	64	32
-	-  	4 	4
-	-  	2 	-
2	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	128	64	32
-	2  	- 	8
-	-  	- 	2
-	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	128	64	32
-	2  	- 	8
-	-  	2 	4
-	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	128	64	32
2	2  	2 	8
-	-  	- 	4
-	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	128	64	32
-	2  	4 	8
-	-  	- 	4
-	-  	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	128	64	32
-	2  	4 	8
-	-  	- 	4
2	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	128	64	32
2	2  	4 	8
-	-  	- 	4
-	-  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	128	64	32
2	2  	4 	8
-	-  	- 	8
-	-  	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	128	64	32
2	2  	4 	16
-	-  	2 	2
-	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	128	64	32
-	4  	4 	16
-	-  	- 	4
-	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	128	64	32
8	16 	- 	-
4	2  	- 	-
2	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	128	64	32
-	-  	8 	16
2	-  	4 	2
-	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	128	64	32
2	2  	8 	16
-	-  	4 	4
-	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	128	64	32
4	8  	16	2
8	-  	- 	-
-	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	128	64	32
4	8  	16	2
-	-  	- 	8
-	2  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	128	64	32
4	8  	16	2
8	-  	- 	-
2	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	128	64	32
4	8  	16	2
-	-  	2 	8
-	-  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	128	64	32
4	8  	16	2
2	8  	- 	2
4	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	64	32
2	16 	16	4
4	-  	- 	-
-	-  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	64	32
-	2  	32	4
2	-  	- 	4
-	-  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	64	32
2	2  	32	8
-	-  	- 	4
-	2  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	64	32
-	4  	32	8
2	-  	- 	4
-	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	64	32
-	4  	32	8
-	-  	2 	4
-	2  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	64	32
-	4  	32	8
-	4  	2 	4
-	-  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	64	32
-	8  	32	8
-	2  	2 	8
-	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	64	32
-	8  	32	16
-	2  	2 	-
-	2  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	64	32
-	8  	32	16
-	-  	- 	4
-	-  	4 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	64	32
2	8  	32	16
-	-  	4 	4
-	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	64	32
2	8  	32	16
2	-  	- 	8
-	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	64	32
4	8  	32	16
-	-  	- 	8
-	-  	2 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	64	32
4	8  	32	16
-	-  	- 	8
-	2  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	64	32
4	8  	32	16
-	-  	- 	8
2	-  	2 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	64	32
4	8  	32	16
2	-  	- 	8
-	-  	4 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	64	32
4	8  	32	16
4	-  	2 	8
-	-  	- 	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	64	32
8	8  	32	16
2	-  	2 	16
-	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	128	64	32
2 	8  	32	32
- 	4  	2 	-
- 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	128	64	64
2 	8  	32	-
- 	4  	2 	-
- 	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	128	128	-
2 	8  	32 	2
4 	2  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	256	- 	-
2 	8  	32	2
4 	2  	2 	-
2 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	256	32	2
2 	8  	2 	-
4 	2  	- 	-
2 	-  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	256	32	2
- 	2  	8 	2
- 	2  	4 	2
- 	-  	2 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	256	32	4
- 	4  	8 	2
- 	2  	4 	4
- 	-  	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	256	32	4
- 	4  	8 	2
- 	-  	2 	8
- 	2  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	256	32	4
4 	8  	2 	4
2 	8  	- 	-
4 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	256	32	8
4 	16 	2 	-
2 	-  	- 	2
4 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	256	32	8
- 	4  	16	2
- 	-  	2 	4
- 	-  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	256	32	8
- 	4  	16	2
- 	-  	2 	8
- 	-  	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	256	32	8
- 	4  	16	2
- 	-  	4 	8
- 	-  	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	256	32	8
- 	4  	16	2
- 	-  	4 	8
- 	-  	4 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	256	32	8
- 	4  	16	2
4 	-  	8 	8
- 	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	256	32	8
- 	4  	16	2
- 	-  	4 	16
2 	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	256	32	8
4 	16 	2 	2
4 	16 	- 	-
4 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	256	32	8
8 	32 	2 	2
4 	-  	2 	-
- 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	256	32	8
- 	8  	32	4
- 	2  	4 	2
- 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	256	64	8
- 	8  	4 	4
- 	2  	- 	2
- 	2  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	256	64	8
- 	8  	4 	4
- 	4  	- 	2
- 	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	256	64	8
- 	8  	4 	4
- 	4  	2 	4
- 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	256	64	8
8 	8  	- 	2
4 	2  	4 	-
- 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	256	64	8
16	2  	- 	-
4 	2  	4 	-
- 	2  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	64	8
4 	4  	4 	-
- 	2  	- 	-
4 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	64	8
8 	4  	4 	-
- 	2  	- 	-
- 	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	64	8
8 	8  	- 	-
2 	-  	- 	-
2 	2  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	64	8
16	2  	- 	-
2 	-  	- 	-
4 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	64	8
- 	-  	16	2
- 	-  	- 	2
- 	2  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	64	8
- 	2  	16	4
- 	-  	2 	4
- 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	64	8
- 	2  	16	8
- 	2  	2 	-
- 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	64	16
- 	4  	16	-
- 	-  	2 	-
- 	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	64	16
- 	-  	4 	16
- 	-  	- 	2
- 	4  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	64	32
- 	4  	4 	4
- 	-  	- 	-
- 	-  	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	64	32
- 	-  	4 	8
- 	-  	- 	-
- 	-  	2 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	64	32
- 	-  	4 	8
- 	-  	- 	-
- 	2  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	64	32
2 	-  	4 	8
- 	-  	- 	-
- 	-  	2 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	64	32
- 	2  	4 	8
- 	-  	- 	2
- 	-  	2 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	64	32
- 	2  	4 	8
- 	-  	2 	2
2 	-  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	64	32
- 	2  	4 	8
- 	-  	- 	4
- 	2  	2 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	64	32
- 	2  	4 	8
- 	2  	- 	4
- 	-  	4 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	64	32
- 	4  	8 	8
- 	-  	2 	8
- 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	64	32
- 	4  	8 	16
- 	-  	2 	-
- 	4  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	64	32
- 	8  	8 	16
- 	2  	2 	-
- 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	64	32
- 	-  	16	16
- 	-  	- 	4
- 	2  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	64	32
- 	-  	- 	32
- 	-  	- 	4
2 	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	64	64
2 	-  	- 	4
- 	-  	- 	2
- 	-  	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	32	256	128
-	- 	2  	4
2	- 	-  	2
-	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	4
2 	4  	-  	-
4 	-  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	4
- 	-  	2  	4
- 	-  	-  	4
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	8
2 	-  	2  	4
- 	-  	-  	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	8
2 	-  	4  	4
- 	-  	-  	2
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	8
2 	-  	4  	4
2 	-  	-  	4
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	8
- 	-  	2  	8
- 	2  	2  	4
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	8
- 	-  	2  	8
- 	-  	4  	4
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	8
- 	4  	2  	8
- 	-  	-  	8
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	16
- 	4  	2  	8
- 	-  	-  	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	16
- 	4  	2  	8
- 	2  	-  	2
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	16
- 	4  	2  	8
2 	2  	-  	4
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	16
- 	4  	2  	8
- 	-  	4  	4
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	16
- 	4  	2  	8
- 	-  	-  	8
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	16
2 	4  	2  	16
- 	2  	-  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	32
2 	4  	2  	2
- 	2  	-  	-
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	2  	4  	4
- 	2  	-  	2
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	-  	2  	8
- 	-  	-  	4
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
2 	-  	2  	8
- 	-  	-  	4
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	32
2 	2  	2  	8
- 	-  	-  	8
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	32
2 	2  	2  	16
- 	-  	-  	-
- 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	2  	4  	16
- 	-  	-  	-
- 	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	2  	4  	16
- 	-  	-  	-
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	32
2 	2  	4  	16
- 	-  	2  	4
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	4  	4  	16
- 	-  	2  	4
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	2  	8  	16
- 	-  	2  	4
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	32
2 	8  	16 	-
2 	4  	-  	-
2 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	2  	8  	16
- 	-  	2  	4
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	32
- 	2  	8  	16
- 	-  	4  	8
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	2  	8  	16
- 	2  	4  	8
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	32
- 	4  	8  	16
- 	-  	4  	8
- 	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	4  	8  	16
2 	-  	4  	8
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	4  	8  	16
- 	2  	4  	8
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	4  	8  	16
- 	2  	4  	8
- 	2  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	4  	8  	16
- 	2  	4  	8
2 	-  	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	32
- 	4  	8  	16
- 	2  	4  	8
2 	-  	2  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	32
2 	4  	8  	16
- 	2  	4  	16
2 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	32
4 	4  	8  	32
- 	2  	4  	-
- 	2  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
4 	4  	8  	-
- 	4  	4  	-
- 	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
2 	-  	8  	8
- 	-  	-  	8
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
2 	-  	8  	16
- 	2  	-  	4
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
2 	2  	8  	16
- 	-  	-  	4
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
- 	4  	8  	16
- 	-  	-  	4
- 	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
- 	4  	8  	16
- 	2  	-  	4
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
- 	4  	8  	16
- 	2  	-  	8
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
4 	8  	16 	2
2 	8  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
4 	16 	16 	2
4 	-  	-  	-
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
- 	4  	32 	2
- 	2  	-  	4
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
2 	4  	32 	2
- 	-  	2  	4
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
2 	4  	32 	2
- 	-  	2  	4
- 	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
2 	4  	32 	2
- 	-  	4  	4
- 	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
2 	4  	32 	2
- 	-  	-  	8
2 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
4 	4  	32 	2
- 	-  	-  	8
- 	2  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
- 	8  	32 	2
- 	2  	-  	8
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
8 	32 	2  	-
2 	8  	-  	-
2 	4  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
- 	8  	32 	2
- 	2  	2  	8
- 	-  	2  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
4 	8  	32 	2
- 	2  	4  	16
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
4 	8  	32 	2
2 	4  	16 	-
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
4 	8  	32 	4
2 	4  	16 	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
4 	8  	32 	4
4 	4  	16 	-
- 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
8 	8  	32 	4
- 	4  	16 	-
2 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
- 	16 	32 	4
- 	-  	4  	16
2 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
16	32 	4  	-
4 	16 	-  	2
2 	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
16	32 	4  	2
4 	16 	-  	-
2 	4  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
16	32 	4  	4
4 	16 	2  	-
2 	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
- 	16 	32 	8
- 	4  	16 	2
2 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
16	32 	8  	-
4 	16 	2  	-
4 	4  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
16	32 	8  	2
8 	16 	2  	2
- 	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
16	32 	8  	2
- 	8  	16 	4
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
16	32 	8  	2
- 	8  	16 	8
- 	4  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
16	32 	8  	2
8 	16 	8  	2
4 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
16	32 	16 	4
8 	16 	-  	-
4 	2  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
16	32 	16 	4
- 	-  	8  	16
2 	4  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
16	32 	16 	4
8 	16 	2  	-
2 	4  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
16	32 	16 	4
2 	8  	16 	2
2 	4  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
16	32 	32 	4
4 	8  	2  	2
- 	4  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
16	64 	4  	-
4 	8  	4  	-
8 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
16	64 	8  	2
4 	8  	-  	-
8 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
16	64 	8  	2
- 	-  	4  	8
2 	-  	8  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
16	64 	8  	2
4 	8  	-  	-
2 	8  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
16	64 	8  	4
4 	16 	2  	-
2 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
16	64 	8  	4
4 	16 	4  	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
16	64 	8  	4
4 	16 	4  	2
- 	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
16	64 	8  	4
4 	16 	4  	4
2 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
16	64 	8  	8
4 	16 	4  	-
2 	2  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
- 	16 	64 	16
- 	4  	16 	4
2 	-  	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
2 	16 	64 	16
- 	4  	16 	8
- 	-  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
2 	16 	64 	16
4 	16 	8  	-
4 	2  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
2 	32 	64 	16
8 	2  	8  	2
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
2 	32 	64 	16
8 	2  	8  	2
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
2 	32 	64 	16
8 	2  	8  	4
2 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
2 	32 	64 	16
8 	2  	8  	4
2 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
2 	32 	64 	16
8 	2  	8  	8
2 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
2 	32 	64 	16
8 	4  	8  	8
2 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
2 	32 	64 	16
4 	8  	4  	16
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
2 	32 	64 	32
4 	8  	4  	4
- 	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
2 	32 	64 	32
- 	4  	8  	8
2 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
2 	32 	64 	32
- 	-  	4  	16
2 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
2 	32 	64 	32
4 	16 	2  	-
4 	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
2 	32 	64 	32
- 	4  	16 	2
- 	2  	-  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
2 	32 	64 	32
4 	16 	2  	-
2 	8  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
2 	32 	64 	32
- 	4  	16 	2
2 	2  	8  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
4 	32 	64 	32
- 	4  	16 	2
2 	2  	8  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
4 	32 	64 	32
4 	16 	2  	2
4 	8  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
8 	32 	64 	32
4 	16 	2  	2
- 	8  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
8 	32 	64 	32
4 	16 	4  	-
8 	4  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
8 	32 	64 	32
- 	4  	16 	4
2 	8  	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
8 	32 	64 	32
2 	4  	16 	8
- 	8  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	128	64
8 	32 	64 	32
2 	4  	16 	8
8 	4  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
8 	32 	64 	32
2 	4  	16 	8
- 	8  	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
8 	32 	64 	32
2 	4  	16 	8
- 	2  	8  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
8 	32 	64 	32
2 	4  	16 	16
- 	2  	8  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	256	128	64
8 	32 	64 	32
2 	2  	4  	32
- 	2  	8  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	64
8 	32 	64 	64
2 	4  	4  	4
- 	2  	8  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	256	128	128
8 	32 	64 	4
2 	4  	4  	-
2 	2  	8  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	256	256	-
8 	32 	64 	4
2 	8  	-  	-
4 	8  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	512	- 	4
8 	32 	64	4
2 	8  	- 	-
4 	8  	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	64	8
8 	32 	2 	-
2 	16 	- 	-
4 	2  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	64	8
- 	8  	32	2
- 	-  	2 	16
- 	2  	4 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	512	64	8
8 	32 	2 	-
2 	16 	- 	-
2 	4  	2 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	64	8
8 	32 	4 	2
4 	16 	2 	-
- 	4  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	64	8
8 	32 	4 	2
2 	4  	16	2
- 	-  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	64	8
8 	32 	4 	4
2 	4  	16	4
- 	2  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	64	8
8 	32 	4 	8
2 	4  	16	-
- 	2  	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	64	16
8 	32 	4 	2
2 	4  	16	-
- 	2  	2 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	512	64	16
8 	32 	4 	2
2 	4  	16	-
4 	2  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	64	16
8 	32 	4 	2
- 	2  	4 	16
- 	2  	4 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	64	16
8 	32 	8 	2
2 	4  	4 	16
- 	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	64	16
8 	32 	8 	2
- 	2  	8 	16
- 	2  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	64	16
8 	32 	16	2
2 	4  	- 	16
- 	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	512	64	16
8 	32 	16	2
2 	4  	16	-
2 	-  	- 	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	64	16
8 	32 	32	2
4 	4  	- 	4
2 	-  	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	64	16
2 	8  	64	2
- 	-  	4 	8
- 	-  	- 	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
2 	8  	4  	2
- 	-  	-  	8
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	16
2 	8  	4  	2
2 	-  	-  	8
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	16
2 	8  	4  	2
- 	-  	2  	8
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
2 	8  	4  	2
2 	-  	4  	8
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
4 	8  	8  	2
- 	-  	2  	8
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
4 	8  	8  	2
- 	-  	2  	8
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
4 	8  	8  	2
- 	-  	4  	8
2 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	16
- 	4  	16 	2
2 	-  	4  	8
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
2 	4  	16 	2
- 	-  	4  	8
- 	2  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	16
2 	4  	16 	2
- 	-  	4  	8
2 	-  	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	16
2 	4  	16 	2
- 	4  	4  	8
- 	-  	2  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
2 	8  	16 	2
- 	-  	4  	16
- 	2  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	512	128	16
2 	8  	16 	2
4 	16 	-  	-
4 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
2 	8  	16 	4
8 	16 	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	16
2 	8  	16 	4
- 	-  	8  	16
- 	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	512	128	16
2 	8  	16 	4
8 	16 	-  	-
4 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
2 	8  	16 	4
8 	16 	2  	-
4 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	16
2 	8  	16 	4
- 	8  	16 	2
- 	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
2 	16 	32 	4
- 	2  	4  	4
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
2 	16 	32 	8
- 	2  	4  	-
- 	2  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	16
2 	16 	32 	8
2 	-  	2  	4
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
4 	16 	32 	8
- 	-  	2  	8
- 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	16
4 	16 	32 	16
- 	2  	2  	-
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	32
4 	16 	32 	-
- 	2  	4  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	32
- 	4  	16 	32
2 	2  	4  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	64
2 	4  	16 	2
- 	2  	4  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	64
2 	4  	16 	4
2 	2  	4  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	64
2 	4  	16 	4
- 	2  	4  	4
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	64
2 	4  	16 	8
- 	2  	4  	-
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	64
2 	4  	16 	8
- 	4  	2  	4
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	64
2 	8  	16 	8
2 	-  	2  	8
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	64
4 	8  	16 	16
2 	-  	2  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	64
- 	4  	8  	32
- 	-  	-  	4
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	64
- 	4  	8  	32
- 	-  	-  	4
- 	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	64
2 	4  	8  	32
- 	-  	-  	4
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	64
2 	4  	8  	32
- 	-  	2  	8
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	512	128	64
2 	4  	8  	32
2 	8  	-  	-
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	64
2 	4  	8  	32
- 	-  	2  	8
4 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	512	128	64
2 	4  	8  	32
2 	8  	-  	2
4 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	64
2 	4  	8  	32
- 	2  	8  	2
4 	-  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	64
2 	4  	16 	32
4 	2  	4  	4
- 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	64
2 	4  	16 	32
- 	4  	2  	8
- 	4  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	64
2 	8  	16 	32
- 	4  	2  	8
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	64
4 	8  	16 	32
- 	4  	2  	8
- 	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	64
4 	8  	16 	32
- 	4  	2  	8
2 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	64
4 	8  	16 	32
2 	4  	2  	8
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	64
4 	8  	16 	32
2 	4  	4  	8
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	512	128	64
4 	8  	16 	32
2 	8  	8  	-
2 	4  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	64
4 	16 	16 	32
4 	4  	8  	2
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	64
- 	4  	32 	32
4 	8  	8  	2
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	128	64
- 	-  	4  	64
- 	4  	16 	2
- 	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	128	128
- 	4  	4  	4
- 	2  	16 	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	512	256	-
8 	4  	-  	-
2 	16 	2  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	256	2
8 	4  	2  	-
4 	16 	-  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	256	2
- 	8  	4  	2
- 	-  	4  	16
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	512	256	4
- 	8  	8  	16
- 	-  	-  	2
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	256	4
- 	-  	16 	16
- 	2  	-  	2
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	512	256	4
- 	-  	-  	32
- 	-  	2  	4
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	512	256	4
32	-  	-  	-
2 	4  	2  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	4
4 	4  	2  	-
4 	-  	-  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	4
- 	-  	8  	2
- 	-  	-  	4
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	512	256	4
8 	2  	-  	2
4 	-  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	4
- 	-  	8  	4
2 	-  	-  	4
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	8
2 	-  	8  	4
- 	2  	-  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	8
- 	2  	8  	4
- 	-  	-  	4
- 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	8
- 	4  	8  	8
4 	-  	-  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	16
4 	4  	8  	-
- 	-  	-  	-
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	16
- 	-  	8  	8
- 	-  	-  	2
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	16
- 	-  	2  	16
- 	-  	-  	2
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	32
2 	-  	2  	4
- 	-  	-  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	32
- 	-  	4  	4
- 	-  	-  	-
- 	-  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	32
- 	-  	-  	8
- 	2  	-  	-
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	32
- 	-  	-  	8
- 	-  	-  	2
2 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	32
- 	2  	-  	8
- 	-  	-  	2
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	32
- 	-  	2  	8
2 	-  	-  	2
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	32
2 	-  	2  	8
- 	-  	-  	4
- 	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	32
2 	-  	4  	8
- 	-  	-  	8
- 	-  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	32
2 	-  	8  	16
- 	-  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	32
4 	-  	8  	16
- 	-  	-  	-
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	32
4 	-  	8  	16
- 	-  	2  	-
- 	-  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	512	256	32
4 	8  	16 	-
2 	-  	-  	-
4 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	32
- 	4  	8  	16
- 	-  	2  	2
- 	-  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	512	256	32
4 	8  	16 	-
4 	-  	-  	-
4 	2  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	32
- 	4  	8  	16
- 	-  	-  	4
- 	2  	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	32
- 	4  	8  	16
- 	2  	4  	8
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	32
- 	4  	8  	16
- 	2  	4  	8
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	512	256	32
4 	8  	16 	-
2 	4  	8  	-
4 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	32
- 	4  	8  	16
- 	2  	4  	8
2 	-  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	512	256	32
4 	8  	16 	-
2 	4  	8  	-
2 	4  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	32
4 	8  	16 	4
4 	8  	8  	-
- 	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	512	256	32
4 	8  	16 	4
4 	16 	-  	-
4 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	32
8 	8  	16 	4
4 	16 	2  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	512	256	32
16	16 	4  	-
4 	16 	4  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	512	256	32
32	4  	-  	2
4 	16 	4  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	32
32	4  	4  	4
4 	16 	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	512	256	32
32	8  	4  	-
4 	16 	-  	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	32
32	8  	4  	2
4 	16 	-  	-
2 	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	512	256	32
32	8  	4  	2
- 	-  	4  	16
- 	2  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	32
32	8  	8  	2
- 	2  	2  	16
- 	2  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	512	256	32
32	16 	2  	-
4 	16 	-  	-
2 	4  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	512	256	32
32	32 	4  	-
4 	4  	-  	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	512	256	32
64	4  	-  	-
8 	2  	2  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	32
8  	4  	2  	-
2  	2  	-  	-
-  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	32
8  	4  	2  	-
2  	4  	-  	-
-  	-  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	32
8  	8  	2  	2
2  	-  	4  	-
-  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	32
16 	4  	-  	-
2  	4  	-  	-
-  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	32
16 	8  	-  	-
2  	2  	-  	-
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	32
-  	-  	16 	8
-  	-  	-  	4
-  	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	32
2  	-  	16 	8
-  	-  	-  	4
-  	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	32
2  	-  	16 	8
-  	-  	2  	8
-  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	32
2  	-  	16 	16
-  	-  	2  	-
-  	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	32
-  	-  	2  	32
2  	-  	-  	2
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
2  	2  	2  	4
-  	-  	-  	-
-  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
-  	2  	4  	4
-  	-  	-  	-
-  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
-  	-  	2  	8
-  	-  	-  	-
2  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
-  	-  	2  	8
-  	-  	-  	-
-  	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
-  	-  	4  	8
-  	-  	-  	4
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
4  	8  	-  	-
4  	-  	-  	-
2  	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
2  	-  	4  	8
-  	-  	-  	4
-  	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
2  	4  	4  	8
-  	-  	-  	8
-  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
2  	4  	4  	16
-  	-  	-  	-
-  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
-  	2  	8  	16
2  	-  	-  	-
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
2  	2  	8  	16
-  	-  	-  	2
-  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
2  	4  	8  	16
-  	-  	-  	2
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
2  	4  	8  	16
2  	-  	-  	-
2  	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
4  	4  	8  	16
2  	-  	2  	-
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
-  	8  	8  	16
2  	-  	-  	4
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
-  	-  	16 	16
-  	-  	2  	4
-  	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
-  	-  	-  	32
-  	-  	2  	4
-  	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
-  	-  	4  	32
-  	-  	-  	8
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
4  	32 	-  	2
8  	-  	-  	-
2  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
-  	4  	32 	2
-  	2  	-  	8
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
4  	32 	2  	-
2  	8  	-  	-
2  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
4  	32 	2  	2
4  	8  	-  	-
2  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
-  	4  	32 	4
-  	2  	4  	8
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
4  	32 	4  	-
2  	4  	8  	-
2  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
4  	32 	4  	2
4  	4  	8  	-
-  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	32 	4  	2
-  	4  	8  	-
2  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	32 	4  	2
2  	-  	4  	8
-  	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	32 	8  	2
2  	-  	-  	8
2  	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
8  	32 	8  	2
2  	8  	-  	-
2  	4  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	32 	8  	2
-  	-  	2  	8
-  	2  	2  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
8  	32 	8  	2
2  	8  	2  	-
4  	8  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	32 	8  	2
2  	2  	8  	2
-  	-  	4  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	32 	16 	4
2  	2  	4  	8
2  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
8  	32 	16 	4
4  	4  	8  	-
2  	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	32 	16 	4
-  	-  	8  	8
-  	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	32 	16 	4
-  	-  	-  	16
4  	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
8  	32 	16 	4
16 	-  	-  	2
4  	2  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	32 	16 	4
-  	2  	16 	2
-  	4  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	32 	32 	4
2  	2  	2  	2
-  	4  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
-  	8  	64 	4
-  	2  	4  	4
-  	-  	-  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
-  	8  	64 	8
-  	2  	4  	8
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
-  	8  	64 	16
-  	2  	4  	2
-  	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
-  	8  	64 	16
2  	2  	4  	2
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
2  	8  	64 	16
-  	2  	4  	4
-  	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
2  	8  	64 	16
-  	-  	2  	8
2  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
2  	8  	64 	16
2  	8  	4  	-
4  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
2  	8  	64 	16
-  	2  	8  	4
-  	2  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
2  	8  	64 	16
-  	4  	8  	8
-  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
2  	8  	64 	16
2  	-  	4  	16
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
4  	8  	64 	32
-  	-  	4  	2
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
4  	8  	64 	32
2  	-  	4  	4
-  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
4  	8  	64 	32
-  	-  	2  	8
-  	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
4  	8  	64 	32
-  	2  	4  	8
-  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
4  	8  	64 	32
2  	4  	8  	-
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
4  	8  	64 	32
-  	2  	4  	8
-  	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
4  	8  	64 	32
-  	4  	4  	8
2  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
4  	8  	64 	32
-  	-  	8  	8
-  	2  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
4  	8  	64 	32
-  	4  	-  	16
-  	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
4  	8  	64 	32
4  	16 	-  	-
2  	4  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
4  	8  	64 	32
-  	-  	4  	16
2  	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
4  	8  	64 	32
2  	2  	8  	16
-  	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
4  	8  	64 	32
-  	4  	8  	16
-  	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
4  	8  	64 	32
4  	8  	16 	2
2  	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	16 	64 	32
2  	4  	16 	2
-  	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	16 	64 	32
2  	8  	16 	2
2  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	16 	64 	32
4  	8  	16 	2
2  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	16 	64 	32
4  	8  	16 	2
-  	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	16 	64 	32
4  	8  	16 	4
-  	2  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	16 	64 	32
4  	8  	16 	4
-  	-  	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	16 	64 	32
4  	8  	16 	8
-  	2  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	16 	64 	32
4  	8  	16 	8
-  	4  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
8  	16 	64 	32
4  	8  	16 	8
4  	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	16 	64 	32
8  	8  	16 	8
-  	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	16 	64 	32
2  	16 	16 	8
-  	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	32 	64 	32
2  	2  	16 	8
-  	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	32 	64 	32
2  	4  	16 	8
-  	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	64
8  	32 	64 	32
2  	4  	16 	8
2  	4  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	32 	64 	32
4  	8  	16 	8
-  	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	32 	64 	32
4  	8  	16 	8
-  	2  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	32 	64 	32
4  	8  	16 	8
-  	2  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	32 	64 	32
4  	8  	16 	8
2  	-  	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	32 	64 	32
4  	8  	16 	8
2  	-  	2  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	32 	64 	32
4  	8  	16 	16
2  	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	64
8  	32 	64 	32
2  	4  	8  	32
-  	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	64
8  	32 	64 	64
2  	4  	8  	4
-  	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
8  	32 	64 	4
2  	4  	8  	2
2  	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
8  	32 	64 	4
2  	4  	8  	2
2  	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	128
8  	32 	64 	4
2  	4  	8  	2
2  	4  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
8  	32 	64 	4
4  	8  	8  	4
-  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
8  	32 	64 	4
-  	4  	16 	4
-  	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
8  	32 	64 	8
-  	4  	16 	2
-  	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
8  	32 	64 	8
-  	4  	16 	4
2  	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
8  	32 	64 	8
-  	4  	16 	4
-  	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
8  	32 	64 	8
-  	4  	16 	8
2  	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
8  	32 	64 	16
2  	4  	16 	-
-  	2  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
8  	32 	64 	16
-  	2  	4  	16
-  	2  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
8  	32 	64 	32
-  	4  	4  	4
2  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
8  	32 	64 	32
2  	4  	4  	4
-  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
8  	32 	64 	32
-  	2  	4  	8
-  	-  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
8  	32 	64 	32
4  	2  	4  	8
-  	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	128
8  	32 	64 	32
4  	2  	4  	8
4  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
8  	32 	64 	32
8  	2  	4  	8
-  	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
16 	32 	64 	32
-  	4  	4  	8
2  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
16 	32 	64 	32
-  	-  	8  	8
2  	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
16 	32 	64 	32
-  	4  	-  	16
-  	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
16 	32 	64 	32
-  	-  	4  	16
2  	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
16 	32 	64 	32
-  	2  	4  	16
-  	-  	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
16 	32 	64 	32
-  	2  	8  	16
2  	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
16 	32 	64 	32
2  	2  	8  	16
-  	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
16 	32 	64 	32
-  	4  	8  	16
2  	-  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
16 	32 	64 	32
2  	4  	8  	16
-  	-  	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
16 	32 	64 	32
2  	4  	8  	16
-  	2  	-  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	512	256	128
16 	32 	64 	32
2  	4  	8  	16
2  	8  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
16 	32 	64 	32
2  	4  	8  	16
2  	2  	8  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
16 	32 	64 	32
4  	4  	16 	16
-  	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
16 	32 	64 	32
-  	-  	8  	32
-  	2  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	128
16 	32 	64 	64
-  	2  	8  	4
-  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	512	256	128
-  	16 	32 	128
-  	2  	8  	4
2  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	512	256	256
2  	16 	32 	4
2  	2  	8  	2
-  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


2	128	512	512
2	16 	32 	4
-	4  	8  	2
-	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	2 	128	1024
2	16	32 	4
-	4 	8  	2
-	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


2	2 	128	1024
-	16	32 	4
-	4 	8  	4
-	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


2	2 	128	1024
-	16	32 	8
-	4 	8  	2
-	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	4 	128	1024
-	16	32 	8
-	4 	8  	2
2	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


2	4 	128	1024
-	16	32 	8
-	4 	8  	4
-	- 	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


2	4 	128	1024
-	16	32 	8
-	4 	8  	4
-	- 	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


2	4 	128	1024
-	16	32 	8
-	4 	8  	8
2	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	4 	128	1024
-	16	32 	16
4	4 	8  	-
-	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	8 	128	1024
-	16	32 	16
-	- 	8  	8
2	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


2	8 	128	1024
2	16	32 	16
-	- 	8  	8
-	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	8 	128	1024
-	16	32 	16
-	2 	8  	8
-	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	8 	128	1024
-	16	32 	16
-	2 	8  	8
-	- 	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	8 	128	1024
2	16	32 	16
-	- 	2  	16
-	- 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	8 	128	1024
2	16	32 	32
-	2 	2  	4
-	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	8	128	1024
-	2	16 	64
-	2	4  	4
-	-	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	8	128	1024
-	4	16 	64
-	-	4  	4
-	-	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	8	128	1024
-	4	16 	64
-	2	-  	8
-	-	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	8 	128	1024
4	16	64 	2
2	8 	-  	-
2	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	8 	128	1024
4	16	64 	2
-	8 	2  	-
-	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	16	128	1024
4	16	64 	2
2	- 	8  	2
-	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	128	1024
2	- 	64 	4
-	- 	8  	-
2	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	32	128	1024
2	64	4  	-
8	- 	-  	-
2	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	128	1024
-	2 	64 	4
-	4 	-  	8
-	- 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	32	128	1024
2	64	4  	-
4	8 	-  	-
4	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	128	1024
-	2 	64 	4
-	2 	4  	8
-	- 	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	128	1024
-	4 	64 	4
-	- 	8  	8
-	2 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4 	32	128	1024
4 	64	4  	-
16	- 	-  	-
4 	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	128	1024
-	4 	64 	4
2	- 	-  	16
-	- 	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	32	128	1024
4	64	4  	-
2	16	2  	-
4	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	32	128	1024
2	64	4  	-
4	16	2  	-
-	2 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	32	128	1024
2	2 	64 	4
-	4 	16 	2
-	- 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


8	32	128	1024
4	64	4  	2
4	16	2  	-
4	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	32	128	1024
8	64	4  	2
4	16	2  	-
-	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	32	128	1024
4 	64	4  	2
- 	16	2  	2
- 	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	32	128	1024
4 	64	4  	4
- 	16	2  	-
- 	2 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	32	128	1024
- 	4 	64 	8
2 	- 	16 	2
- 	- 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	32	128	1024
4 	64	8  	-
2 	16	2  	-
4 	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	32	128	1024
4 	64	8  	-
2 	16	4  	-
4 	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	32	128	1024
- 	4 	64 	8
2 	2 	16 	4
- 	- 	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	32	128	1024
4 	64	8  	2
4 	16	4  	-
4 	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	32	128	1024
8 	64	8  	2
4 	16	4  	-
4 	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	32	128	1024
8 	64	8  	2
8 	16	4  	-
- 	2 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	32	128	1024
16	64	8  	2
- 	16	4  	-
2 	2 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	32	128	1024
2 	64	8  	2
- 	16	4  	-
- 	2 	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


2	64	128	1024
2	64	8  	2
-	- 	16 	4
-	- 	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	128	128	1024
-	2  	8  	2
-	-  	16 	8
-	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	4	256	1024
-	2	8  	2
-	-	16 	8
-	2	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


-	4	256	1024
2	4	8  	2
-	-	16 	8
-	-	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


2	8	256	1024
-	-	8  	2
-	-	16 	8
2	-	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	8	256	1024
-	-	8  	2
-	-	16 	8
-	-	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4 	8	256	1024
8 	2	-  	-
16	8	-  	-
4 	-	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4 	8	256	1024
8 	2	2  	2
16	8	-  	-
4 	-	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	8	256	1024
-	8	2  	4
-	-	16 	8
-	-	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	16	256	1024
-	2 	2  	4
-	- 	16 	8
-	- 	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4 	16	256	1024
4 	4 	-  	-
16	8 	-  	-
2 	4 	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8 	16	256	1024
16	4 	4  	-
2 	8 	-  	2
- 	4 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	16	256	1024
-	2 	16 	8
-	2 	8  	2
-	- 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	16	256	1024
-	4 	16 	8
2	- 	8  	2
-	- 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


8	16	256	1024
4	16	8  	-
2	8 	2  	-
4	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	32	256	1024
4	8 	8  	-
2	- 	4  	-
4	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	32	256	1024
4	8 	8  	-
2	2 	4  	-
4	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	32	256	1024
-	- 	4  	16
2	- 	4  	4
-	- 	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


8	32	256	1024
4	16	-  	-
2	8 	-  	-
4	2 	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	32	256	1024
-	- 	4  	16
-	- 	2  	8
4	4 	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	32	256	1024
4	4 	4  	16
-	- 	4  	8
-	- 	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


8	32	256	1024
8	4 	16 	2
4	8 	-  	-
2	4 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	32	256	1024
4 	4 	16 	2
2 	8 	4  	-
- 	4 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	32	256	1024
8 	16	2  	-
2 	8 	4  	2
4 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	32	256	1024
2 	8 	16 	2
2 	8 	4  	2
- 	- 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	32	256	1024
4 	16	16 	4
- 	- 	4  	4
- 	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	32	256	1024
4 	16	16 	8
- 	2 	4  	-
- 	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	32	256	1024
4 	32	8  	-
2 	4 	-  	2
2 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	64	256	1024
4 	4 	8  	2
4 	- 	-  	-
- 	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	64	256	1024
8 	4 	8  	2
- 	- 	2  	2
- 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	64	256	1024
8 	4 	8  	2
4 	- 	-  	-
- 	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	64	256	1024
8 	4 	8  	2
4 	- 	-  	-
2 	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	64	256	1024
8 	4 	8  	2
4 	- 	-  	-
4 	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	64	256	1024
8 	4 	8  	4
8 	- 	-  	2
- 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	64	256	1024
16	4 	8  	4
2 	- 	-  	2
- 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	256	1024
2 	4 	8  	4
- 	- 	-  	2
- 	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	256	1024
2 	4 	8  	4
2 	- 	-  	-
2 	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	256	1024
4 	4 	8  	4
2 	- 	2  	-
- 	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	256	1024
8 	8 	4  	-
4 	- 	-  	-
2 	- 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	256	1024
16	4 	-  	-
4 	- 	-  	2
2 	4 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	256	1024
16	8 	-  	2
4 	- 	-  	-
2 	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	256	1024
16	8 	-  	4
4 	- 	2  	-
2 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	256	1024
16	8 	4  	-
4 	2 	2  	-
2 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	256	1024
16	8 	4  	-
4 	2 	2  	-
2 	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	256	1024
16	8 	4  	-
4 	2 	4  	-
2 	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	64	256	1024
16	8 	8  	2
4 	2 	-  	-
2 	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	256	1024
16	16	2  	2
4 	2 	-  	-
4 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	64	256	1024
32	4 	-  	-
4 	2 	-  	-
4 	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	64	256	1024
8 	4 	-  	-
2 	4 	-  	-
- 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	128	256	1024
-	-  	8  	4
-	-  	2  	4
-	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


-	128	256	1024
-	-  	8  	8
-	-  	2  	2
-	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	128	256	1024
-	-  	-  	16
-	-  	-  	4
4	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	128	256	1024
-	-  	-  	16
-	-  	2  	4
-	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4 	128	256	1024
16	-  	2  	-
2 	4  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4 	128	256	1024
16	4  	2  	-
4 	-  	2  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	128	256	1024
4	16 	4  	2
-	-  	4  	2
-	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	256	1024
2	16 	8  	4
-	-  	-  	-
-	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 4


-	2  	-  	-
-	-  	-  	-
8	128	256	1024
2	16 	8  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	2  	256	1024
2	128	8  	4
-	16 	-  	-
-	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	2  	256	1024
2	128	8  	8
-	16 	-  	2
-	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	2	256	1024
-	2	128	16
-	-	16 	2
-	-	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	2	256	1024
-	2	128	16
-	-	16 	2
-	-	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	256	1024
-	-	128	16
2	-	16 	4
-	-	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
-	-	128	16
-	2	16 	4
-	4	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	256	1024
4	2	128	16
-	4	16 	4
-	-	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


8	4 	256	1024
4	2 	128	16
4	16	4  	-
2	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
4	2	128	16
-	4	16 	4
2	-	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	256	1024
4	2	128	16
2	4	16 	8
-	-	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
4	2	128	16
2	4	16 	8
-	-	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
4	2	128	16
2	4	16 	8
-	2	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
4	2	128	16
2	4	16 	8
-	2	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
4	2	128	16
2	4	16 	8
-	2	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
4	2	128	16
2	4	16 	8
-	2	2  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	256	1024
4	2	128	16
2	4	16 	16
-	2	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	256	1024
4	2	128	32
2	4	16 	2
-	2	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	256	1024
4	2	128	32
2	4	16 	4
2	2	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
4	2	128	32
2	4	16 	4
-	2	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	256	1024
4	2	128	32
2	4	16 	8
-	2	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
4	2	128	32
2	4	16 	8
-	2	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
4	2	128	32
2	4	16 	8
-	2	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
4	2	128	32
2	4	16 	8
-	2	2  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	256	1024
4	2	128	32
2	4	16 	16
2	2	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
4	2	128	32
-	2	4  	32
4	-	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	4	256	1024
8	4	128	64
-	-	4  	4
-	-	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	4	256	1024
8	4	128	64
-	-	-  	8
-	-	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	8	256	1024
- 	-	128	64
- 	2	2  	8
- 	-	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
- 	-	128	64
- 	-	4  	8
2 	-	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
- 	-	128	64
- 	2	4  	8
- 	-	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
- 	-	128	64
- 	2	4  	8
- 	2	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
- 	-	128	64
2 	2	4  	8
- 	-	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
- 	-	128	64
- 	4	4  	8
- 	-	2  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	8	256	1024
2 	4	128	64
- 	-	4  	16
- 	-	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
2 	4	128	64
- 	-	4  	16
2 	-	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
2 	4	128	64
2 	-	4  	16
- 	-	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
2 	4	128	64
- 	2	4  	16
- 	2	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
2 	4	128	64
- 	2	4  	16
- 	2	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
2 	4	128	64
2 	2	4  	16
- 	-	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
2 	4	128	64
- 	4	4  	16
- 	-	2  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	8 	256	1024
2 	4 	128	64
8 	16	-  	2
2 	8 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
2 	4	128	64
- 	8	16 	2
- 	2	2  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	8 	256	1024
2 	4 	128	64
8 	16	2  	-
4 	8 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	8 	256	1024
2 	4 	128	64
8 	16	2  	2
4 	8 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
2 	4	128	64
- 	8	16 	4
2 	4	8  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	8	256	1024
4 	4	128	64
- 	8	16 	8
2 	4	8  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


16	8	256	1024
2 	8	128	64
- 	8	16 	8
- 	2	4  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	16	256	1024
2 	8 	128	64
- 	2 	16 	16
- 	- 	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


2	32	256	1024
2	8 	128	64
-	- 	2  	32
-	- 	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


2	32	256	1024
2	8 	128	64
2	32	-  	-
4	2 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


2	32	256	1024
2	8 	128	64
-	2 	2  	32
-	- 	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	256	1024
-	8 	128	64
-	2 	2  	32
-	4 	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	256	1024
-	8 	128	64
-	- 	4  	32
-	2 	4  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	256	1024
-	8 	128	64
-	2 	8  	32
-	- 	2  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	32 	256	1024
8	128	64 	-
2	8  	32 	-
2	8  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32 	256	1024
8	128	64 	4
4	16 	32 	-
-	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	32 	256	1024
8	128	64 	4
4	16 	32 	-
2	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	32 	256	1024
8	128	64 	4
4	16 	32 	-
4	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32 	256	1024
8	128	64 	4
8	16 	32 	-
2	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4 	32 	256	1024
16	128	64 	4
2 	16 	32 	-
- 	2  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4 	32 	256	1024
16	128	64 	4
2 	16 	32 	-
4 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4 	32 	256	1024
16	128	64 	4
- 	2  	16 	32
- 	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4 	32 	256	1024
16	128	64 	4
- 	4  	16 	32
- 	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4 	32 	256	1024
16	128	64 	4
4 	16 	32 	-
2 	4  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4 	32 	256	1024
16	128	64 	4
- 	4  	16 	32
2 	2  	4  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4 	32 	256	1024
16	128	64 	4
- 	4  	16 	32
- 	2  	4  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4 	32 	256	1024
16	128	64 	4
4 	16 	32 	2
2 	4  	8  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4 	32 	256	1024
16	128	64 	4
4 	16 	32 	2
2 	2  	4  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4 	32 	256	1024
16	128	64 	4
4 	16 	32 	2
- 	4  	4  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4 	32 	256	1024
16	128	64 	4
4 	16 	32 	2
- 	4  	8  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4 	32 	256	1024
16	128	64 	4
4 	16 	32 	2
4 	-  	4  	16

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4 	32 	256	1024
16	128	64 	4
4 	16 	32 	2
8 	16 	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4 	32 	256	1024
16	128	64 	4
4 	32 	32 	2
8 	2  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4 	32 	256	1024
16	128	64 	4
2 	4  	64 	2
- 	8  	2  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4 	32 	256	1024
16	128	128	4
2 	4  	2  	2
2 	8  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	256	1024
-	16	256	4
2	2 	4  	4
-	2 	8  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	512	1024
2	16	4  	8
-	4 	8  	4
-	- 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	512	1024
2	16	4  	8
-	4 	8  	8
-	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	512	1024
2	16	4  	16
-	4 	8  	2
-	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	32	512	1024
2	16	4  	16
4	8 	2  	-
2	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	512	1024
2	16	4  	16
4	8 	4  	-
2	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	512	1024
2	16	8  	16
4	8 	-  	2
2	2 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	512	1024
2	16	8  	16
2	4 	8  	2
-	- 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	512	1024
4	16	16 	16
-	4 	2  	2
-	- 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	512	1024
-	4 	16 	32
-	- 	4  	4
-	2 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	32	512	1024
-	4 	16 	32
-	2 	4  	8
2	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	512	1024
-	4 	16 	32
2	2 	4  	8
-	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	512	1024
-	4 	16 	32
2	4 	4  	8
-	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	512	1024
-	4 	16 	32
-	2 	8  	8
-	2 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


4	32	512	1024
-	4 	16 	32
-	- 	2  	16
2	- 	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


4	32	512	1024
4	16	32 	-
2	16	-  	-
2	4 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	32	512	1024
4	32	32 	2
-	4 	2  	-
-	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	32	512	1024
-	4 	64 	2
-	4 	4  	2
-	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	32	512	1024
-	8 	64 	4
-	- 	4  	-
-	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


8	32	512	1024
8	64	4  	-
4	- 	2  	-
2	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	32	512	1024
4 	64	4  	-
2 	- 	2  	-
- 	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	32	512	1024
4 	64	4  	-
4 	- 	-  	2
2 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	32	512	1024
8 	64	4  	2
2 	- 	2  	-
- 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	32	512	1024
8 	64	4  	2
4 	- 	-  	2
- 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	32	512	1024
8 	64	4  	2
4 	2 	-  	2
- 	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	32	512	1024
8 	64	4  	2
4 	4 	-  	-
- 	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	32	512	1024
8 	64	4  	2
8 	- 	-  	-
2 	- 	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	32	512	1024
16	64	4  	2
2 	- 	2  	-
- 	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	32	512	1024
2 	64	4  	4
- 	- 	2  	-
- 	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


2	64	512	1024
-	2 	64 	8
-	- 	-  	2
-	- 	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


2	64	512	1024
2	64	8  	-
2	- 	2  	-
2	- 	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


4	128	512	1024
4	-  	8  	2
-	-  	2  	-
-	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	512	1024
2	-  	8  	2
-	-  	2  	-
-	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	512	1024
-	2  	8  	2
-	-  	-  	2
-	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	512	1024
-	2  	8  	4
-	-  	2  	-
-	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	512	1024
-	2  	8  	4
-	-  	2  	2
-	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	512	1024
-	2  	8  	4
-	-  	2  	4
-	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	512	1024
-	4  	8  	8
-	-  	2  	-
-	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


8	128	512	1024
-	-  	4  	16
2	-  	-  	2
-	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


8	128	512	1024
4	16 	-  	-
4	-  	-  	-
2	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


8	128	512	1024
8	16 	-  	2
2	-  	-  	2
-	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	128	512	1024
2 	16 	-  	4
- 	-  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	128	512	1024
4 	16 	-  	4
2 	-  	-  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	128	512	1024
4 	16 	4  	-
2 	-  	-  	-
- 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	128	512	1024
4 	16 	4  	-
2 	-  	-  	-
2 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	128	512	1024
4 	16 	4  	-
4 	2  	-  	-
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	128	512	1024
8 	16 	4  	-
4 	2  	2  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	128	512	1024
8 	16 	4  	2
4 	4  	-  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


16	128	512	1024
8 	16 	4  	2
8 	2  	-  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


16	128	512	1024
16	16 	4  	2
- 	2  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	128	512	1024
2 	16 	4  	2
- 	2  	-  	-
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	128	512	1024
2 	16 	4  	2
2 	2  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	128	512	1024
4 	16 	4  	2
2 	2  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	128	512	1024
4 	16 	4  	2
4 	2  	-  	-
- 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	128	512	1024
8 	16 	4  	2
2 	4  	-  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


32	128	512	1024
8 	16 	4  	2
- 	2  	2  	4
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	128	512	1024
8 	16 	4  	2
4 	4  	4  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	128	512	1024
8 	16 	4  	2
8 	4  	-  	-
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


32	128	512	1024
16	16 	4  	2
- 	4  	2  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


32	128	512	1024
32	4  	2  	-
4 	4  	-  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
4 	8  	2  	2
- 	-  	-  	-
- 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
4 	8  	4  	-
- 	-  	-  	-
2 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
4 	8  	4  	-
2 	-  	2  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
4 	8  	4  	-
4 	2  	-  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
8 	8  	4  	2
- 	2  	2  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	4  	2  	-
4 	-  	-  	-
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	4  	2  	2
4 	-  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	4  	4  	-
4 	-  	-  	-
2 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	8  	-  	-
4 	-  	-  	-
4 	-  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	8  	4  	-
8 	-  	-  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	8  	4  	-
8 	2  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	8  	4  	-
8 	2  	2  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	8  	4  	-
8 	4  	-  	-
2 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	8  	4  	2
8 	4  	2  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	8  	4  	2
8 	4  	2  	-
2 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	8  	4  	2
8 	4  	2  	-
4 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	8  	4  	2
8 	4  	4  	-
4 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	8  	8  	2
8 	4  	2  	-
4 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	128	512	1024
- 	16 	16 	2
- 	8  	4  	2
- 	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
32	2  	-  	-
8 	4  	2  	-
2 	4  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
32	2  	4  	2
8 	8  	-  	-
2 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
32	2  	4  	2
16	-  	-  	-
2 	4  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
32	2  	4  	4
16	4  	4  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
32	2  	8  	4
16	4  	-  	-
2 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	128	512	1024
32	2  	8  	4
- 	-  	16 	4
- 	2  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
32	4  	8  	8
- 	-  	16 	4
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
32	4  	16 	-
16	4  	-  	-
2 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
32	8  	16 	-
16	-  	2  	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
32	8  	16 	-
16	4  	-  	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
32	8  	16 	-
16	4  	2  	-
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
32	8  	16 	-
16	4  	2  	-
4 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
32	8  	16 	-
16	4  	4  	-
4 	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
32	8  	16 	-
16	8  	2  	-
8 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	128	512	1024
2 	32 	8  	16
- 	16 	8  	2
- 	-  	-  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
2 	32 	16 	16
2 	16 	-  	2
- 	-  	-  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	128	512	1024
2 	2  	32 	32
- 	2  	16 	2
- 	-  	-  	8

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
4 	64 	-  	-
2 	16 	2  	-
8 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	128	512	1024
- 	-  	4  	64
- 	2  	16 	2
- 	2  	8  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
- 	4  	4  	64
- 	-  	16 	4
- 	-  	8  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
8 	64 	-  	-
16	4  	-  	-
8 	2  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
8 	64 	-  	2
16	4  	-  	-
8 	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
8 	64 	-  	2
16	8  	-  	-
8 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	128	512	1024
- 	8  	64 	2
- 	-  	16 	8
2 	-  	8  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
8 	64 	2  	-
16	8  	2  	-
2 	8  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
8 	64 	4  	-
16	16 	2  	-
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
8 	64 	4  	-
32	2  	2  	-
4 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	128	512	1024
- 	8  	64 	4
- 	2  	32 	4
- 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
- 	8  	64 	8
- 	2  	32 	4
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
8 	64 	8  	-
2 	32 	4  	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
8 	64 	8  	2
4 	32 	4  	-
- 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
8 	64 	8  	2
4 	32 	4  	-
2 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
8 	64 	8  	2
4 	32 	4  	2
4 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
8 	64 	8  	4
8 	32 	4  	-
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	64 	8  	4
- 	32 	4  	-
2 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	64 	8  	4
2 	32 	4  	-
2 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	64 	8  	4
4 	32 	4  	2
- 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	64 	8  	4
4 	32 	4  	2
2 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	64 	8  	4
4 	32 	4  	2
4 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	64 	8  	4
8 	32 	4  	4
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	64 	8  	4
8 	32 	8  	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	64 	16 	4
8 	32 	2  	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	128	512	1024
16	64 	16 	4
- 	8  	32 	4
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	64 	16 	8
2 	8  	32 	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	64 	16 	8
4 	8  	32 	2
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	64 	16 	8
4 	8  	32 	4
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	64 	16 	8
4 	8  	32 	4
2 	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	64 	16 	8
4 	8  	32 	8
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	64 	16 	16
4 	8  	32 	2
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	64 	32 	-
4 	8  	32 	2
4 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	128	512	1024
16	64 	64 	2
8 	8  	-  	-
2 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	128	512	1024
16	128	2  	-
16	-  	-  	2
4 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	256	512	1024
32	-  	2  	2
4 	-  	-  	2
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	4  	-  	-
4 	2  	-  	-
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	256	512	1024
32	4  	-  	2
4 	2  	-  	-
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	4  	2  	-
4 	2  	-  	-
2 	-  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	256	512	1024
32	4  	2  	-
4 	2  	4  	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	256	512	1024
- 	32 	4  	2
4 	2  	4  	2
- 	4  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	4  	2  	-
4 	2  	4  	2
4 	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	256	512	1024
32	4  	2  	4
8 	4  	4  	-
- 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	256	512	1024
32	8  	2  	4
8 	2  	4  	-
- 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	8  	2  	4
8 	2  	4  	-
2 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	8  	2  	4
8 	2  	4  	-
4 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	8  	2  	4
8 	2  	4  	-
4 	2  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	8  	2  	4
8 	2  	4  	2
4 	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	8  	2  	4
8 	2  	4  	2
8 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	256	512	1024
32	8  	2  	4
16	2  	4  	4
- 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	8  	2  	4
16	2  	8  	2
2 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	256	512	1024
32	8  	2  	4
16	2  	8  	2
- 	-  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	8  	2  	4
16	2  	8  	2
4 	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	256	512	1024
32	8  	2  	4
16	4  	8  	4
4 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


64	256	512	1024
32	8  	2  	4
16	4  	8  	4
2 	-  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	8  	2  	4
16	4  	8  	4
2 	4  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	256	512	1024
32	8  	2  	8
16	8  	8  	2
2 	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	8  	2  	8
16	16 	2  	-
4 	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


64	256	512	1024
32	8  	2  	8
32	2  	2  	-
4 	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


64	256	512	1024
64	8  	4  	8
4 	4  	2  	-
- 	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
4  	8  	4  	8
-  	4  	2  	-
2  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
4  	8  	4  	8
4  	2  	-  	2
2  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
8  	8  	4  	8
2  	2  	-  	2
-  	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
16 	4  	8  	-
4  	2  	2  	-
2  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
16 	4  	8  	-
4  	4  	-  	2
2  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
16 	4  	8  	-
8  	2  	-  	2
2  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
16 	4  	8  	-
8  	4  	-  	-
2  	-  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
16 	4  	8  	2
8  	4  	-  	-
2  	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
16 	8  	8  	2
8  	4  	-  	-
2  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
16 	16 	2  	-
8  	4  	2  	-
4  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
32 	2  	-  	-
8  	4  	2  	-
4  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
32 	2  	-  	-
8  	4  	2  	-
4  	2  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
32 	2  	-  	-
8  	4  	2  	-
4  	4  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
32 	2  	2  	2
8  	8  	-  	-
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
32 	4  	2  	2
16 	-  	-  	-
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
32 	4  	4  	-
16 	-  	-  	2
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
32 	8  	-  	4
16 	2  	-  	-
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
32 	8  	4  	-
16 	2  	2  	-
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
32 	8  	4  	2
16 	4  	-  	-
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	256	512	1024
32 	8  	4  	2
4  	-  	16 	4
-  	-  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
32 	8  	4  	2
4  	16 	4  	2
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
32 	8  	8  	4
8  	16 	-  	4
-  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
32 	8  	8  	8
8  	16 	2  	-
-  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
32 	16 	8  	-
8  	16 	2  	-
2  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
32 	32 	8  	-
8  	2  	2  	-
2  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	8  	-  	-
8  	4  	-  	2
4  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	8  	2  	-
8  	4  	2  	-
4  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	8  	2  	-
8  	4  	2  	-
4  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	8  	2  	-
8  	4  	2  	-
4  	2  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	8  	2  	2
8  	4  	2  	-
4  	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	8  	4  	-
8  	4  	2  	-
8  	-  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
64 	8  	4  	4
16 	4  	2  	-
4  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	8  	8  	-
16 	4  	2  	-
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	16 	-  	-
16 	4  	2  	2
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	16 	-  	2
16 	4  	4  	-
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	16 	2  	2
16 	8  	-  	-
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	16 	4  	-
16 	8  	-  	-
4  	2  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
64 	16 	4  	2
16 	8  	2  	-
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	256	512	1024
64 	16 	4  	2
-  	16 	8  	2
-  	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
64 	32 	4  	4
2  	2  	8  	2
-  	-  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	32 	8  	2
4  	8  	2  	-
4  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	256	512	1024
64 	32 	8  	2
-  	4  	8  	2
-  	2  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
64 	32 	16 	4
2  	4  	-  	4
-  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
64 	32 	16 	8
2  	4  	-  	-
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	256	512	1024
64 	32 	16 	8
-  	-  	2  	4
-  	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	32 	16 	8
2  	4  	-  	-
2  	4  	2  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
64 	32 	16 	8
4  	8  	2  	2
-  	-  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	256	512	1024
64 	32 	16 	8
-  	4  	8  	4
2  	-  	-  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	32 	16 	8
4  	8  	4  	-
4  	2  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	256	512	1024
64 	32 	16 	8
-  	4  	8  	4
2  	-  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	32 	16 	8
4  	8  	4  	4
2  	4  	2  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


128	256	512	1024
64 	32 	16 	8
2  	4  	8  	8
-  	2  	4  	2

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


128	256	512	1024
64 	32 	16 	16
2  	4  	8  	2
2  	2  	4  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	32 	32 	-
2  	4  	8  	2
4  	4  	-  	4

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
64 	64 	2  	-
2  	4  	8  	2
8  	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1


128	256	512	1024
128	2  	2  	-
2  	4  	8  	2
8  	4  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 3


256	256	512	1024
2  	2  	2  	2
8  	8  	8  	2
-  	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	512	512	1024
2	-  	4  	4
-	8  	16 	2
-	-  	-  	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	-	1024	1024
-	4	2   	8
-	8	16  	2
-	-	-   	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 2


-	-	- 	2048
-	4	2 	8
2	8	16	2
-	-	- 	-

Choose a movement:
	[1] Left
	[2] Right
	[3] Up
	[4] Down

Choice: 1
Game won after 945 moves!
Final Board:
[[None, None, None, 2048], [None, 4, 2, 8], [2, 8, 16, 2], [None, None, None, None]]
>>>
```
</details>