{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "aecc23a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1. Import the NUMPY package under the name np."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3e5970c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "78438039",
   "metadata": {},
   "outputs": [],
   "source": [
    "#2. Print the NUMPY version and the configuration."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "45310eab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1.23.5'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.__version__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "440ddf66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "blas_armpl_info:\n",
      "  NOT AVAILABLE\n",
      "blas_mkl_info:\n",
      "  NOT AVAILABLE\n",
      "blis_info:\n",
      "  NOT AVAILABLE\n",
      "openblas_info:\n",
      "    libraries = ['openblas', 'openblas']\n",
      "    library_dirs = ['/Users/borja/anaconda3/lib']\n",
      "    language = c\n",
      "    define_macros = [('HAVE_CBLAS', None)]\n",
      "blas_opt_info:\n",
      "    libraries = ['openblas', 'openblas']\n",
      "    library_dirs = ['/Users/borja/anaconda3/lib']\n",
      "    language = c\n",
      "    define_macros = [('HAVE_CBLAS', None)]\n",
      "lapack_armpl_info:\n",
      "  NOT AVAILABLE\n",
      "lapack_mkl_info:\n",
      "  NOT AVAILABLE\n",
      "openblas_lapack_info:\n",
      "    libraries = ['openblas', 'openblas']\n",
      "    library_dirs = ['/Users/borja/anaconda3/lib']\n",
      "    language = c\n",
      "    define_macros = [('HAVE_CBLAS', None)]\n",
      "lapack_opt_info:\n",
      "    libraries = ['openblas', 'openblas']\n",
      "    library_dirs = ['/Users/borja/anaconda3/lib']\n",
      "    language = c\n",
      "    define_macros = [('HAVE_CBLAS', None)]\n",
      "Supported SIMD extensions in this NumPy install:\n",
      "    baseline = SSE,SSE2,SSE3\n",
      "    found = SSSE3,SSE41,POPCNT,SSE42,AVX,F16C,FMA3,AVX2\n",
      "    not found = AVX512F,AVX512CD,AVX512_KNL,AVX512_SKX,AVX512_CLX,AVX512_CNL,AVX512_ICL\n"
     ]
    }
   ],
   "source": [
    "np.show_config()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e8c33c3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable \"a\"\n",
    "# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9fd6127c",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.random.rand(2,3,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a1102019",
   "metadata": {},
   "outputs": [],
   "source": [
    "#4. Print a."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "017c181f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0.36095974 0.07213914 0.28440562 0.85512954 0.29557375]\n",
      "  [0.31489504 0.95060645 0.42878325 0.60334186 0.79047125]\n",
      "  [0.18331283 0.39313918 0.44315603 0.97675122 0.80003639]]\n",
      "\n",
      " [[0.84262181 0.73184676 0.99866759 0.77147504 0.51569538]\n",
      "  [0.47205667 0.97461859 0.28195991 0.51314291 0.56291914]\n",
      "  [0.13289569 0.89486149 0.11821735 0.41504341 0.93059943]]]\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0f123351",
   "metadata": {},
   "outputs": [],
   "source": [
    "#5. Create a 5x2x3 3-dimensional array with all values equaling 1.\n",
    "#Assign the array to variable \"b\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ed7ac739",
   "metadata": {},
   "outputs": [],
   "source": [
    "b = np.ones((5,2,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "39dc1495",
   "metadata": {},
   "outputs": [],
   "source": [
    "#6. Print b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3cb9aee2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[1. 1. 1.]\n",
      "  [1. 1. 1.]]\n",
      "\n",
      " [[1. 1. 1.]\n",
      "  [1. 1. 1.]]\n",
      "\n",
      " [[1. 1. 1.]\n",
      "  [1. 1. 1.]]\n",
      "\n",
      " [[1. 1. 1.]\n",
      "  [1. 1. 1.]]\n",
      "\n",
      " [[1. 1. 1.]\n",
      "  [1. 1. 1.]]]\n"
     ]
    }
   ],
   "source": [
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0c2ea0df",
   "metadata": {},
   "outputs": [],
   "source": [
    "#7. Do a and b have the same size? How do you prove that in Python code?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b57c2e98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f747a242",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "56e3e4c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.size == b.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "2f8ba367",
   "metadata": {},
   "outputs": [],
   "source": [
    "#8. Are you able to add a and b? Why or why not?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "db837401",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "operands could not be broadcast together with shapes (2,3,5) (5,2,3) ",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[19], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m m \u001b[38;5;241m=\u001b[39m \u001b[43ma\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m \u001b[49m\u001b[43mb\u001b[49m\n",
      "\u001b[0;31mValueError\u001b[0m: operands could not be broadcast together with shapes (2,3,5) (5,2,3) "
     ]
    }
   ],
   "source": [
    "m = a + b  #las dimensiones no coinciden"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "840f74c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe \"c\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "c36dfff0",
   "metadata": {},
   "outputs": [],
   "source": [
    "c = b.T "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "d281574f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 2, 5)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "3a9e00f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#10. Try to add a and c. Now it should work. Assign the sum to varialbe \"d\". But why does it work now?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "67246ec2",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = a + c.reshape(2,3,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "76b9c641",
   "metadata": {},
   "outputs": [],
   "source": [
    "#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "d2b268cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0.36095974 0.07213914 0.28440562 0.85512954 0.29557375]\n",
      "  [0.31489504 0.95060645 0.42878325 0.60334186 0.79047125]\n",
      "  [0.18331283 0.39313918 0.44315603 0.97675122 0.80003639]]\n",
      "\n",
      " [[0.84262181 0.73184676 0.99866759 0.77147504 0.51569538]\n",
      "  [0.47205667 0.97461859 0.28195991 0.51314291 0.56291914]\n",
      "  [0.13289569 0.89486149 0.11821735 0.41504341 0.93059943]]]\n"
     ]
    }
   ],
   "source": [
    "print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "b40cae80",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[1.36095974 1.07213914 1.28440562 1.85512954 1.29557375]\n",
      "  [1.31489504 1.95060645 1.42878325 1.60334186 1.79047125]\n",
      "  [1.18331283 1.39313918 1.44315603 1.97675122 1.80003639]]\n",
      "\n",
      " [[1.84262181 1.73184676 1.99866759 1.77147504 1.51569538]\n",
      "  [1.47205667 1.97461859 1.28195991 1.51314291 1.56291914]\n",
      "  [1.13289569 1.89486149 1.11821735 1.41504341 1.93059943]]]\n"
     ]
    }
   ],
   "source": [
    "print(d) #ha sumado cada valor de una matriz por el valor en la misma posición de la otra matriz."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "72217935",
   "metadata": {},
   "outputs": [],
   "source": [
    "#12. Multiply a and c. Assign the result to e."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "662142d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "e = a * c.reshape(2,3,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "cbfb8e1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0.36095974 0.07213914 0.28440562 0.85512954 0.29557375]\n",
      "  [0.31489504 0.95060645 0.42878325 0.60334186 0.79047125]\n",
      "  [0.18331283 0.39313918 0.44315603 0.97675122 0.80003639]]\n",
      "\n",
      " [[0.84262181 0.73184676 0.99866759 0.77147504 0.51569538]\n",
      "  [0.47205667 0.97461859 0.28195991 0.51314291 0.56291914]\n",
      "  [0.13289569 0.89486149 0.11821735 0.41504341 0.93059943]]]\n"
     ]
    }
   ],
   "source": [
    "print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d538003d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#13. Does e equal to a? Why or why not?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "3170e8a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[ True,  True,  True,  True,  True],\n",
       "        [ True,  True,  True,  True,  True],\n",
       "        [ True,  True,  True,  True,  True]],\n",
       "\n",
       "       [[ True,  True,  True,  True,  True],\n",
       "        [ True,  True,  True,  True,  True],\n",
       "        [ True,  True,  True,  True,  True]]])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "e == a #estás multiplicndo cada valor por 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "daa29747",
   "metadata": {},
   "outputs": [],
   "source": [
    "#14. Identify the max, min, and mean values in d. Assign those values to variables \"d_max\", \"d_min\", and \"d_mean\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "47e52f30",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.9986675861390468"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d_max = d.max()\n",
    "\n",
    "d_max"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "48511b61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0721391440090011"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d_min = d.min()\n",
    "\n",
    "d_min"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "aa678f1d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.563644082660205"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d_mean = d.mean()\n",
    "\n",
    "d_mean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "c839f020",
   "metadata": {},
   "outputs": [],
   "source": [
    "#15. Now we want to label the values in d. First create an empty array \"f\" with the same shape (i.e. 2x3x5) as d using `np.empty`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "e27d4a8d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[0.36095974, 0.07213914, 0.28440562, 0.85512954, 0.29557375],\n",
       "        [0.31489504, 0.95060645, 0.42878325, 0.60334186, 0.79047125],\n",
       "        [0.18331283, 0.39313918, 0.44315603, 0.97675122, 0.80003639]],\n",
       "\n",
       "       [[0.84262181, 0.73184676, 0.99866759, 0.77147504, 0.51569538],\n",
       "        [0.47205667, 0.97461859, 0.28195991, 0.51314291, 0.56291914],\n",
       "        [0.13289569, 0.89486149, 0.11821735, 0.41504341, 0.93059943]]])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f = np.empty((2,3,5))\n",
    "\n",
    "f"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "da75035f",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.\n",
    "If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.\n",
    "If a value equals to d_mean, assign 50 to the corresponding value in f.\n",
    "Assign 0 to the corresponding value(s) in f for d_min in d.\n",
    "Assign 100 to the corresponding value(s) in f for d_max in d.\n",
    "In the end, f should have only the following values: 0, 25, 50, 75, and 100.\n",
    "Note: you don't have to use Numpy in this question.\n",
    "\"\"\"\n",
    "\n",
    "for i in range(d.shape[0]):\n",
    "    for j in range(d.shape[1]):\n",
    "        for k in range(d.shape[2]):\n",
    "        \n",
    "            if d[i,j,k] > d_min and d[i,j,k] < d_mean:\n",
    "                f[i,j,k] = 25\n",
    "            elif d[i,j,k] > d_mean and d[i,j,k] < d_max:\n",
    "                f[i,j,k] = 75\n",
    "            elif d[i,j,k] == d_mean:\n",
    "                f[i,j,k] = 50\n",
    "            elif d[i,j,k] == d_min:\n",
    "                f[i,j,k] = 0\n",
    "            elif d[i,j,k] == d_max:\n",
    "                f[i,j,k] = 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "1cf811ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "#17. Print d and f. Do you have your expected f?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "93002f57",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 25.   0.  25.  75.  25.]\n",
      "  [ 25.  75.  25.  75.  75.]\n",
      "  [ 25.  25.  25.  75.  75.]]\n",
      "\n",
      " [[ 75.  75. 100.  75.  25.]\n",
      "  [ 25.  75.  25.  25.  25.]\n",
      "  [ 25.  75.  25.  25.  75.]]]\n"
     ]
    }
   ],
   "source": [
    "print(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "4fa6bc72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[1.36095974 1.07213914 1.28440562 1.85512954 1.29557375]\n",
      "  [1.31489504 1.95060645 1.42878325 1.60334186 1.79047125]\n",
      "  [1.18331283 1.39313918 1.44315603 1.97675122 1.80003639]]\n",
      "\n",
      " [[1.84262181 1.73184676 1.99866759 1.77147504 1.51569538]\n",
      "  [1.47205667 1.97461859 1.28195991 1.51314291 1.56291914]\n",
      "  [1.13289569 1.89486149 1.11821735 1.41504341 1.93059943]]]\n"
     ]
    }
   ],
   "source": [
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21e4da59",
   "metadata": {},
   "outputs": [],
   "source": [
    "#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values \n",
    "(\"A\", \"B\", \"C\", \"D\", and \"E\") to label the array elements? You are expecting the result to be:"
   ]
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
