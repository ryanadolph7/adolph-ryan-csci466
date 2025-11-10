Ryan Adolph, Programming Assigment 3 - Link Layer Token Passing Protocol

To run this code: 

Depending on python version: python or python3

python3 node.py (sending port) (receiving port) (number of packets) (is node head? - 1 or 0) (node number)

	(repeat this on multiple command lines linking the sending and receiving ports into a loop)

To end the program(s), use Control C (^C) to end on all command lines.

for example: 

(terminal 1)
python3 node.py 8001 8000 5 1 1

(terminal 2)
python3 node.py 8002 8001 1 0 2

(terminal 3)
python3 node.py 8003 8002 3 0 3

(terminal 4)
python3 node.py 8004 8003 0 0 4

(terminal 5) 
python3 node.py 8000 8004 1 1 4


Link for video demonstration of code -- 
https://montana.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d098ae4c-2b68-469c-bcad-b3910035be8f
