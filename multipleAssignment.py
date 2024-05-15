{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "96b4a41b-fc32-4af5-a052-7308d91997a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "class multipleAssignment():\n",
    "    def oddEven():\n",
    "        num=int(input(\"enter the number:\"))\n",
    "        if((num%2)==1):\n",
    "            print(num,\"is odd number\")\n",
    "            message=\"odd number\"\n",
    "        else:\n",
    "            print(num,\"is even number\")\n",
    "            message=\"even number\"\n",
    "        return message\n",
    "    def percentage():\n",
    "        subject1=int(input(\"subject1:\"))\n",
    "        subject2=int(input(\"subject2:\"))\n",
    "        subject3=int(input(\"subject3:\"))\n",
    "        subject4=int(input(\"subject4:\"))\n",
    "        subject5=int(input(\"subject5:\"))\n",
    "        total=subject1+subject2+subject3+subject4+subject5\n",
    "        print(\"total:\",total)\n",
    "        percentage=total/5\n",
    "        print(\"percentage:\",percentage)\n",
    "    def elegible():\n",
    "        gender=input(\"your gender:\")\n",
    "        age=int(input(\"your age\"))\n",
    "        if(gender in \"male\"):\n",
    "            if(age<21):\n",
    "                print(\"not eligible\")\n",
    "                message=\"not eligible\"\n",
    "            else:\n",
    "                print(\"eligible\")\n",
    "                message=\"eligible\"\n",
    "        elif(gender in \"female\"):\n",
    "             if(age<18):\n",
    "                 print(\"not eligible\")\n",
    "                 message=\"not eligible\"\n",
    "             else:\n",
    "                 print(\"eligible\")\n",
    "        else:\n",
    "            print(\"invalid gender\")\n",
    "            message=\"invalid gender\"\n",
    "        return message\n",
    "    def subfieldsInAI():\n",
    "        lists=(\"machine lerning\",\"neural learning\",\"vision\",\"robotics\",\"speech processing\",\"natural language processing\")\n",
    "        field=\"sub-field in ai are:\"\n",
    "        print(field)\n",
    "        for field in lists:\n",
    "            print(field)\n",
    "    def triangle():\n",
    "        height=int(input(\"height:\"))\n",
    "        breath=int(input(\"breath:\"))\n",
    "        print(\"area of formula:(breath*height)/2\")\n",
    "        area=(breath*height)/2\n",
    "        print(\"area of triangle:\",area)\n",
    "        height1=int(input(\"height1:\"))\n",
    "        height2=int(input(\"height2:\"))\n",
    "        breath1=int(input(\"breath1:\"))\n",
    "        print(\"perimeter of triangle=height1+height2+breath1\")\n",
    "        perimeter=height1+height2+breath1\n",
    "        print(\"perimeter of triangle:\",perimeter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "166da6a3-28d7-4ba6-91a1-7fa3027195ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sub-field in ai are:\n",
      "machine lerning\n",
      "neural learning\n",
      "vision\n",
      "robotics\n",
      "speech processing\n",
      "natural language processing\n"
     ]
    }
   ],
   "source": [
    "multipleAssignment.subfieldsInAI()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5d53e1c1-6523-48e7-8aee-5460eb26e062",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the number: 52452\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "52452 is even number\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'even number'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "multipleAssignment.oddEven()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b6162a93-b6e7-486e-ab5c-57005b4b1acc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "your gender: male\n",
      "your age 20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "not eligible\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'not eligible'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "multipleAssignment.elegible()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c397bffe-5b08-4489-8818-55fd892ddf24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "subject1: 98\n",
      "subject2: 87\n",
      "subject3: 95\n",
      "subject4: 95\n",
      "subject5: 93\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total: 468\n",
      "percentage: 93.6\n"
     ]
    }
   ],
   "source": [
    "multipleAssignment.percentage()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d1a04a8a-7085-4411-a6ad-88a3b5bf0dd7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "height: 32\n",
      "breath: 34\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "area of formula:(breath*height)/2\n",
      "area of triangle: 544.0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "height1: 2\n",
      "height2: 4\n",
      "breath1: 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "perimeter of triangle=height1+height2+breath1\n",
      "perimeter of triangle: 10\n"
     ]
    }
   ],
   "source": [
    "multipleAssignment.triangle()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62226f1f-4f51-4632-a90b-37b40423c178",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
