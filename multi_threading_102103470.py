{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'numpy'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mtime\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mthreading\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'numpy'"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting numpyNote: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "  Obtaining dependency information for numpy from https://files.pythonhosted.org/packages/16/2e/86f24451c2d530c88daf997cb8d6ac622c1d40d19f5a031ed68a4b73a374/numpy-1.26.4-cp312-cp312-win_amd64.whl.metadata\n",
      "  Downloading numpy-1.26.4-cp312-cp312-win_amd64.whl.metadata (61 kB)\n",
      "     ---------------------------------------- 0.0/61.0 kB ? eta -:--:--\n",
      "     --------------------------------- ------ 51.2/61.0 kB 1.3 MB/s eta 0:00:01\n",
      "     ---------------------------------------- 61.0/61.0 kB 1.1 MB/s eta 0:00:00\n",
      "Downloading numpy-1.26.4-cp312-cp312-win_amd64.whl (15.5 MB)\n",
      "   ---------------------------------------- 0.0/15.5 MB ? eta -:--:--\n",
      "    --------------------------------------- 0.2/15.5 MB 7.6 MB/s eta 0:00:03\n",
      "   - -------------------------------------- 0.6/15.5 MB 6.0 MB/s eta 0:00:03\n",
      "   -- ------------------------------------- 0.9/15.5 MB 7.2 MB/s eta 0:00:03\n",
      "   --- ------------------------------------ 1.3/15.5 MB 6.6 MB/s eta 0:00:03\n",
      "   --- ------------------------------------ 1.5/15.5 MB 6.9 MB/s eta 0:00:03\n",
      "   ---- ----------------------------------- 1.9/15.5 MB 6.6 MB/s eta 0:00:03\n",
      "   ----- ---------------------------------- 2.2/15.5 MB 6.6 MB/s eta 0:00:03\n",
      "   ------ --------------------------------- 2.5/15.5 MB 6.8 MB/s eta 0:00:02\n",
      "   ------- -------------------------------- 2.8/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   ------- -------------------------------- 3.1/15.5 MB 7.0 MB/s eta 0:00:02\n",
      "   -------- ------------------------------- 3.4/15.5 MB 7.0 MB/s eta 0:00:02\n",
      "   --------- ------------------------------ 3.8/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   ---------- ----------------------------- 4.1/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   ----------- ---------------------------- 4.4/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   ------------ --------------------------- 4.7/15.5 MB 7.0 MB/s eta 0:00:02\n",
      "   ------------ --------------------------- 5.0/15.5 MB 6.8 MB/s eta 0:00:02\n",
      "   ------------- -------------------------- 5.3/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   -------------- ------------------------- 5.6/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   --------------- ------------------------ 5.9/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   --------------- ------------------------ 6.2/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   ---------------- ----------------------- 6.5/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   ----------------- ---------------------- 6.7/15.5 MB 7.0 MB/s eta 0:00:02\n",
      "   ------------------ --------------------- 7.1/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   ------------------- -------------------- 7.4/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   ------------------- -------------------- 7.7/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   -------------------- ------------------- 8.0/15.5 MB 6.8 MB/s eta 0:00:02\n",
      "   --------------------- ------------------ 8.3/15.5 MB 6.9 MB/s eta 0:00:02\n",
      "   ---------------------- ----------------- 8.7/15.5 MB 6.8 MB/s eta 0:00:02\n",
      "   ----------------------- ---------------- 9.0/15.5 MB 6.9 MB/s eta 0:00:01\n",
      "   ----------------------- ---------------- 9.3/15.5 MB 6.9 MB/s eta 0:00:01\n",
      "   ------------------------ --------------- 9.6/15.5 MB 6.9 MB/s eta 0:00:01\n",
      "   ------------------------- -------------- 10.0/15.5 MB 6.9 MB/s eta 0:00:01\n",
      "   -------------------------- ------------- 10.3/15.5 MB 6.9 MB/s eta 0:00:01\n",
      "   --------------------------- ------------ 10.6/15.5 MB 7.0 MB/s eta 0:00:01\n",
      "   ---------------------------- ----------- 10.9/15.5 MB 7.0 MB/s eta 0:00:01\n",
      "   ---------------------------- ----------- 11.2/15.5 MB 7.0 MB/s eta 0:00:01\n",
      "   ----------------------------- ---------- 11.4/15.5 MB 6.9 MB/s eta 0:00:01\n",
      "   ------------------------------ --------- 11.6/15.5 MB 6.8 MB/s eta 0:00:01\n",
      "   ------------------------------ --------- 12.0/15.5 MB 6.8 MB/s eta 0:00:01\n",
      "   ------------------------------- -------- 12.3/15.5 MB 6.8 MB/s eta 0:00:01\n",
      "   -------------------------------- ------- 12.6/15.5 MB 6.9 MB/s eta 0:00:01\n",
      "   --------------------------------- ------ 12.9/15.5 MB 6.8 MB/s eta 0:00:01\n",
      "   --------------------------------- ------ 13.2/15.5 MB 6.9 MB/s eta 0:00:01\n",
      "   ---------------------------------- ----- 13.5/15.5 MB 6.8 MB/s eta 0:00:01\n",
      "   ----------------------------------- ---- 13.9/15.5 MB 6.8 MB/s eta 0:00:01\n",
      "   ------------------------------------ --- 14.2/15.5 MB 6.8 MB/s eta 0:00:01\n",
      "   ------------------------------------- -- 14.5/15.5 MB 6.8 MB/s eta 0:00:01\n",
      "   -------------------------------------- - 14.8/15.5 MB 6.9 MB/s eta 0:00:01\n",
      "   ---------------------------------------  15.2/15.5 MB 6.9 MB/s eta 0:00:01\n",
      "   ---------------------------------------  15.5/15.5 MB 6.9 MB/s eta 0:00:01\n",
      "   ---------------------------------------  15.5/15.5 MB 6.9 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 15.5/15.5 MB 6.7 MB/s eta 0:00:00\n",
      "Installing collected packages: numpy\n",
      "Successfully installed numpy-1.26.4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  WARNING: The script f2py.exe is installed in 'c:\\Users\\Adhyan\\AppData\\Local\\Programs\\Python\\Python312\\Scripts' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\n",
      "\n",
      "[notice] A new release of pip is available: 23.2.1 -> 24.0\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "%pip install numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting matplotlib\n",
      "  Obtaining dependency information for matplotlib from https://files.pythonhosted.org/packages/7d/ca/e7bd1876a341ed8c456095962a582696cac1691cb6e55bd5ead15a755c5d/matplotlib-3.8.4-cp312-cp312-win_amd64.whl.metadata\n",
      "  Downloading matplotlib-3.8.4-cp312-cp312-win_amd64.whl.metadata (5.9 kB)\n",
      "Collecting contourpy>=1.0.1 (from matplotlib)\n",
      "  Obtaining dependency information for contourpy>=1.0.1 from https://files.pythonhosted.org/packages/78/38/a046bb0ebce6f530175d434e7364149e338ffe1069ee286ed8ba7f6481ee/contourpy-1.2.1-cp312-cp312-win_amd64.whl.metadata\n",
      "  Downloading contourpy-1.2.1-cp312-cp312-win_amd64.whl.metadata (5.8 kB)\n",
      "Collecting cycler>=0.10 (from matplotlib)\n",
      "  Obtaining dependency information for cycler>=0.10 from https://files.pythonhosted.org/packages/e7/05/c19819d5e3d95294a6f5947fb9b9629efb316b96de511b418c53d245aae6/cycler-0.12.1-py3-none-any.whl.metadata\n",
      "  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)\n",
      "Collecting fonttools>=4.22.0 (from matplotlib)\n",
      "  Obtaining dependency information for fonttools>=4.22.0 from https://files.pythonhosted.org/packages/56/85/0a77382e3dd8528d7f13ee97415c82b36c4879023f226e2b98d012fce077/fonttools-4.51.0-cp312-cp312-win_amd64.whl.metadata\n",
      "  Downloading fonttools-4.51.0-cp312-cp312-win_amd64.whl.metadata (162 kB)\n",
      "     ---------------------------------------- 0.0/162.8 kB ? eta -:--:--\n",
      "     ---------------------- ---------------- 92.2/162.8 kB 2.6 MB/s eta 0:00:01\n",
      "     -------------------------------------- 162.8/162.8 kB 3.2 MB/s eta 0:00:00\n",
      "Collecting kiwisolver>=1.3.1 (from matplotlib)\n",
      "  Obtaining dependency information for kiwisolver>=1.3.1 from https://files.pythonhosted.org/packages/63/50/2746566bdf4a6a842d117367d05c90cfb87ac04e9e2845aa1fa21f071362/kiwisolver-1.4.5-cp312-cp312-win_amd64.whl.metadata\n",
      "  Downloading kiwisolver-1.4.5-cp312-cp312-win_amd64.whl.metadata (6.5 kB)\n",
      "Requirement already satisfied: numpy>=1.21 in c:\\users\\adhyan\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from matplotlib) (1.26.4)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\adhyan\\appdata\\roaming\\python\\python312\\site-packages (from matplotlib) (24.0)\n",
      "Collecting pillow>=8 (from matplotlib)\n",
      "  Obtaining dependency information for pillow>=8 from https://files.pythonhosted.org/packages/d3/23/3927d888481ff7c44fdbca3bc2a2e97588c933db46723bf115201377c436/pillow-10.3.0-cp312-cp312-win_amd64.whl.metadata\n",
      "  Downloading pillow-10.3.0-cp312-cp312-win_amd64.whl.metadata (9.4 kB)\n",
      "Collecting pyparsing>=2.3.1 (from matplotlib)\n",
      "  Obtaining dependency information for pyparsing>=2.3.1 from https://files.pythonhosted.org/packages/9d/ea/6d76df31432a0e6fdf81681a895f009a4bb47b3c39036db3e1b528191d52/pyparsing-3.1.2-py3-none-any.whl.metadata\n",
      "  Downloading pyparsing-3.1.2-py3-none-any.whl.metadata (5.1 kB)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in c:\\users\\adhyan\\appdata\\roaming\\python\\python312\\site-packages (from matplotlib) (2.9.0.post0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\adhyan\\appdata\\roaming\\python\\python312\\site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)\n",
      "Downloading matplotlib-3.8.4-cp312-cp312-win_amd64.whl (7.7 MB)\n",
      "   ---------------------------------------- 0.0/7.7 MB ? eta -:--:--\n",
      "   - -------------------------------------- 0.2/7.7 MB 7.6 MB/s eta 0:00:01\n",
      "   -- ------------------------------------- 0.6/7.7 MB 7.2 MB/s eta 0:00:01\n",
      "   ---- ----------------------------------- 0.9/7.7 MB 7.2 MB/s eta 0:00:01\n",
      "   ------ --------------------------------- 1.2/7.7 MB 7.1 MB/s eta 0:00:01\n",
      "   ------- -------------------------------- 1.5/7.7 MB 7.2 MB/s eta 0:00:01\n",
      "   --------- ------------------------------ 1.8/7.7 MB 7.2 MB/s eta 0:00:01\n",
      "   ----------- ---------------------------- 2.1/7.7 MB 6.7 MB/s eta 0:00:01\n",
      "   ------------ --------------------------- 2.4/7.7 MB 6.9 MB/s eta 0:00:01\n",
      "   -------------- ------------------------- 2.7/7.7 MB 6.7 MB/s eta 0:00:01\n",
      "   --------------- ------------------------ 3.1/7.7 MB 6.9 MB/s eta 0:00:01\n",
      "   ----------------- ---------------------- 3.4/7.7 MB 6.8 MB/s eta 0:00:01\n",
      "   ------------------ --------------------- 3.6/7.7 MB 6.8 MB/s eta 0:00:01\n",
      "   -------------------- ------------------- 3.9/7.7 MB 6.7 MB/s eta 0:00:01\n",
      "   ---------------------- ----------------- 4.3/7.7 MB 6.8 MB/s eta 0:00:01\n",
      "   ------------------------ --------------- 4.6/7.7 MB 6.8 MB/s eta 0:00:01\n",
      "   ------------------------- -------------- 4.9/7.7 MB 6.9 MB/s eta 0:00:01\n",
      "   --------------------------- ------------ 5.2/7.7 MB 6.8 MB/s eta 0:00:01\n",
      "   ---------------------------- ----------- 5.5/7.7 MB 6.9 MB/s eta 0:00:01\n",
      "   ------------------------------ --------- 5.8/7.7 MB 6.9 MB/s eta 0:00:01\n",
      "   -------------------------------- ------- 6.1/7.7 MB 6.9 MB/s eta 0:00:01\n",
      "   --------------------------------- ------ 6.5/7.7 MB 6.9 MB/s eta 0:00:01\n",
      "   ----------------------------------- ---- 6.8/7.7 MB 6.9 MB/s eta 0:00:01\n",
      "   ------------------------------------- -- 7.1/7.7 MB 6.9 MB/s eta 0:00:01\n",
      "   -------------------------------------- - 7.4/7.7 MB 6.9 MB/s eta 0:00:01\n",
      "   ---------------------------------------  7.7/7.7 MB 6.9 MB/s eta 0:00:01\n",
      "   ---------------------------------------  7.7/7.7 MB 6.9 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 7.7/7.7 MB 6.4 MB/s eta 0:00:00\n",
      "Downloading contourpy-1.2.1-cp312-cp312-win_amd64.whl (189 kB)\n",
      "   ---------------------------------------- 0.0/189.9 kB ? eta -:--:--\n",
      "   ---------------------------------------- 189.9/189.9 kB 5.8 MB/s eta 0:00:00\n",
      "Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)\n",
      "Downloading fonttools-4.51.0-cp312-cp312-win_amd64.whl (2.2 MB)\n",
      "   ---------------------------------------- 0.0/2.2 MB ? eta -:--:--\n",
      "   ---- ----------------------------------- 0.3/2.2 MB 7.9 MB/s eta 0:00:01\n",
      "   ----------- ---------------------------- 0.6/2.2 MB 6.4 MB/s eta 0:00:01\n",
      "   ------------------ --------------------- 1.0/2.2 MB 6.9 MB/s eta 0:00:01\n",
      "   ------------------------ --------------- 1.3/2.2 MB 7.0 MB/s eta 0:00:01\n",
      "   ---------------------------- ----------- 1.6/2.2 MB 6.7 MB/s eta 0:00:01\n",
      "   ----------------------------------- ---- 1.9/2.2 MB 7.2 MB/s eta 0:00:01\n",
      "   ---------------------------------------  2.2/2.2 MB 6.9 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 2.2/2.2 MB 6.6 MB/s eta 0:00:00\n",
      "Downloading kiwisolver-1.4.5-cp312-cp312-win_amd64.whl (56 kB)\n",
      "   ---------------------------------------- 0.0/56.0 kB ? eta -:--:--\n",
      "   ---------------------------------------- 56.0/56.0 kB 3.1 MB/s eta 0:00:00\n",
      "Downloading pillow-10.3.0-cp312-cp312-win_amd64.whl (2.5 MB)\n",
      "   ---------------------------------------- 0.0/2.5 MB ? eta -:--:--\n",
      "   ---- ----------------------------------- 0.3/2.5 MB 8.6 MB/s eta 0:00:01\n",
      "   --------- ------------------------------ 0.6/2.5 MB 7.6 MB/s eta 0:00:01\n",
      "   ----------- ---------------------------- 0.7/2.5 MB 5.9 MB/s eta 0:00:01\n",
      "   ---------------- ----------------------- 1.1/2.5 MB 6.2 MB/s eta 0:00:01\n",
      "   ---------------------- ----------------- 1.4/2.5 MB 6.4 MB/s eta 0:00:01\n",
      "   -------------------------- ------------- 1.7/2.5 MB 6.4 MB/s eta 0:00:01\n",
      "   ------------------------------- -------- 2.0/2.5 MB 6.7 MB/s eta 0:00:01\n",
      "   ------------------------------------ --- 2.3/2.5 MB 6.8 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 2.5/2.5 MB 6.4 MB/s eta 0:00:00\n",
      "Downloading pyparsing-3.1.2-py3-none-any.whl (103 kB)\n",
      "   ---------------------------------------- 0.0/103.2 kB ? eta -:--:--\n",
      "   ---------------------------------------- 103.2/103.2 kB 5.8 MB/s eta 0:00:00\n",
      "Installing collected packages: pyparsing, pillow, kiwisolver, fonttools, cycler, contourpy, matplotlib\n",
      "Successfully installed contourpy-1.2.1 cycler-0.12.1 fonttools-4.51.0 kiwisolver-1.4.5 matplotlib-3.8.4 pillow-10.3.0 pyparsing-3.1.2\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  WARNING: The scripts fonttools.exe, pyftmerge.exe, pyftsubset.exe and ttx.exe are installed in 'c:\\Users\\Adhyan\\AppData\\Local\\Programs\\Python\\Python312\\Scripts' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\n",
      "\n",
      "[notice] A new release of pip is available: 23.2.1 -> 24.0\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "%pip install matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: psutil in c:\\users\\adhyan\\appdata\\roaming\\python\\python312\\site-packages (5.9.8)Note: you may need to restart the kernel to use updated packages.\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 23.2.1 -> 24.0\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "%pip install psutil"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import time\n",
    "import threading\n",
    "import matplotlib.pyplot as plt\n",
    "import psutil"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def multiply_matrices(matrix, constant_matrix, result, start, end):\n",
    "    for i in range(start, end):\n",
    "        result[i] = np.dot(matrix[i], constant_matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Time taken with 1 threads: 1.2639505863189697 seconds\n",
      "Time taken with 2 threads: 0.9028809070587158 seconds\n",
      "Time taken with 3 threads: 0.950192928314209 seconds\n",
      "Time taken with 4 threads: 0.9496574401855469 seconds\n",
      "Time taken with 5 threads: 0.966731071472168 seconds\n",
      "Time taken with 6 threads: 0.9655108451843262 seconds\n",
      "Time taken with 7 threads: 0.9695291519165039 seconds\n",
      "Time taken with 8 threads: 1.015026569366455 seconds\n"
     ]
    }
   ],
   "source": [
    "def multiply_with_threads(matrix, constant_matrix, num_threads):\n",
    "    result = [None] * len(matrix)\n",
    "    threads = []\n",
    "    chunk_size = len(matrix) // num_threads\n",
    "\n",
    "    for i in range(num_threads):\n",
    "        start = i * chunk_size\n",
    "        end = start + chunk_size if i < num_threads - 1 else len(matrix)\n",
    "        thread = threading.Thread(target=multiply_matrices, args=(matrix, constant_matrix, result, start, end))\n",
    "        threads.append(thread)\n",
    "        thread.start()\n",
    "\n",
    "    for thread in threads:\n",
    "        thread.join()\n",
    "\n",
    "    return result\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    num_matrices = 100\n",
    "    matrix_size = 1000\n",
    "    constant_matrix = np.random.rand(matrix_size, matrix_size)\n",
    "    matrices = [np.random.rand(matrix_size, matrix_size) for _ in range(num_matrices)]\n",
    "\n",
    "    num_threads_list = [1, 2,3, 4,5,6,7, 8]  # Adjust this list according to your CPU capabilities\n",
    "    times = []\n",
    "\n",
    "    for num_threads in num_threads_list:\n",
    "        start_time = time.time()\n",
    "        result = multiply_with_threads(matrices, constant_matrix, num_threads)\n",
    "        end_time = time.time()\n",
    "        times.append(end_time - start_time)\n",
    "\n",
    "        print(f\"Time taken with {num_threads} threads: {end_time - start_time} seconds\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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RwsAhJCQEEGtVuu2jxgxQrCxsREKCgoEQRCE3NxcwdXVVRg3bpze+6SmpgouLi5ltj/KggULBABCYmKiblt+fn6Z/caPHy84ODjoahAEQejWrZsQHBwsCIIgbNy4UbC2thbGjRsnaDQa3T7PPPOM0KpVK73XabVaoVOnTkKTJk1021atWiUAEHr27ClotVrd9rfeektQKBR641SesLAwoV27dnrbjh49KgAQvvvuO0EQBOHUqVMCAOGnn356ZFvlGT16tODo6CgIgiB8++23AgBh06ZNuucBCBMmTCjTnwfHVRAE4c8//xQACH/++aduW7du3QQAwtq1a3XbLly4IAAQ5HK5cPjwYd32HTt2CACEVatW6bbNmjVLACD0799f773++9//CgCE06dPC4IgCFevXhUUCoXw0Ucf6e135swZwcrKSm97aU3Lly+v1Pi0adNG8PDwEG7fvq3bdvr0aUEulwujRo0q0/+q/h2U9zktVfrzVLduXSEzM1O3/ZdffhEACFu3btVtGz16tABAmDZtml4bf/31lwBA+OGHH/S2x8bGltlemZ+PoqIiwcPDQ2jTpo1QWFio22/FihUCAKFbt266bQMGDND9HFHtxyNARCg5DeDi4qJ73LFjRwAl84usrKz0thcVFSEpKQkAsGvXLmRlZWHEiBHIyMjQfSkUCnTs2BF//vlnteqyt7fXfZ+bm4uMjAx06dIF+fn5uHDhQpn9161bh2HDhmH8+PH46quvIJeX/IhnZmbijz/+wNChQ3XtZGRk4Pbt2wgPD0dCQoKuT6VeffVVvbk1Xbp0gUajKff01oOGDRuGEydO4PLly7pt69evh62tLQYMGAAAurHesWMH8vPzqzgq973wwgtGPwrk5OSE4cOH6x43a9YMrq6uaNGihe5zAdz/jFy5cqVMGxMmTNB7/MYbbwAomUAMAJs2bYJWq8XQoUP1PjdeXl5o0qRJmc+Nra0txo4d+9jaU1JSEBcXhzFjxsDNzU23vXXr1ujVq5fu/U1t2LBhqFOnju5xly5dAJQ/Vq+//rre459++gkuLi7o1auX3ti0a9cOTk5OemNTmZ+P48ePIz09Ha+99hpsbGx0+48ZM0bvZx4omQ918+bNMqfrqHZiACIC0KBBA73Hpf8w+vn5lbv9wXksAPD000/D3d1d72vnzp26iaaGio+Px6BBg+Di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5SzZ8uXL0a5dO3z11Vd47733YGVlhYYNG+LFF19E586dAVTt5+PVV1+FRqPBggUL8Pbbb6NVq1b49ddf8f777+vtN378ePzwww9YtGgRVCoV6tevj0mTJmHGjBlm6zuZj0ww1rWjRERERDUE5wARERGR5DAAERERkeQwABEREZHkMAARERGR5DAAERERkeQwABEREZHk8D5A5dBqtUhOToazs3OF6wgRERGRZREEAbm5ufDx8SmzztzDGIDKkZycXGblZyIiIqoZbty48dhFlRmAylF6y/MbN25AqVQatW21Wo2dO3fqbu8uNVLvP8AxYP+l3X+AYyD1/gOmG4OcnBz4+flVaukSBqBylJ72UiqVJglADg4OUCqVkvzgS73/AMeA/Zd2/wGOgdT7D5h+DCozfYWToImIiEhyGICIiIhIchiAiIiISHIYgIiIiEhyGICIiIhIchiAiIiISHIYgIiIiEhyGICIiIhIchiAiIiISHIYgMxIoxVwJDETJzJkOJKYCY1WELskIiIiSeJSGGYSezYFMVvPISW7AIAC3yUch7eLHWZFBqFPS2+xyyMiIpIUHgEyg9izKXj9+5P3ws99qdkFeP37k4g9myJSZURERNLEAGRiGq2AmK3nUN7JrtJtMVvP8XQYERGRGTEAmdjRxMwyR34eJABIyS7A0cRM8xVFREQkcQxAJpaeW3H4MWQ/IiIiqj4GIBPzcLYz6n5ERERUfQxAJtYhwA3eLnaQVfC8DIC3ix06BLiZsywiIiJJYwAyMYVchlmRQQBQJgSVPp4VGQSFvKKIRERERMbGAGQGfVp648sX28LLRf80l5eLHb58sS3vA0RERGRmvBGimfRp6Y1eQV5Y9se/WLT7Enxd7bD/nad55IeIiEgEPAJkRgq5DINDfQAAqTmFUGu0IldEREQkTQxAZubhbAsnawEarYALqblil0NERCRJDEBmJpPJUN+h5K7P8cnZIldDREQkTaIGoP379yMyMhI+Pj6QyWTYsmXLI/fftGkTevXqBXd3dyiVSoSFhWHHjh16+8yePRsymUzvq3nz5ibsRdXVdyz5Mz45R9xCiIiIJErUAJSXl4eQkBAsW7asUvvv378fvXr1wu+//44TJ06gR48eiIyMxKlTp/T2Cw4ORkpKiu7rwIEDpijfYPUdS48AMQARERGJQdSrwCIiIhAREVHp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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#The graph showing the relation between number of threads and time taken\n",
    "plt.plot(num_threads_list, times, marker='o')\n",
    "plt.xlabel('Number of Threads')\n",
    "plt.ylabel('Time Taken (seconds)')\n",
    "plt.title('Time Taken vs Number of Threads')\n",
    "plt.grid(True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CPU Usage: [2.7, 2.7, 2.1, 2.3, 2.1, 1.7, 1.9, 1.9]\n"
     ]
    }
   ],
   "source": [
    "#For monitoring cpu usage\n",
    "cpu_usage = [psutil.cpu_percent(interval=1) for _ in range(len(num_threads_list))]\n",
    "print(\"CPU Usage:\", cpu_usage)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}