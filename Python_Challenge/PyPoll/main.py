{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ab29a42-6b79-4a17-aa94-4fdfebdf7062",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# import libraries\n",
    "import os \n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6407b972-1897-4dca-ac71-6f76ecf799d0",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# open csv file\n",
    "election_csv = os.path.join(\"Resources\",\"election_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6f5fb8b-131c-4a91-be1a-f4b6b06874e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# list to store data\n",
    "totalv = 0\n",
    "cdts = {}\n",
    "winner = \"\"\n",
    "mvotes = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26e47fd3-1068-4b0c-bae9-d4ed1c5a5567",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# open and read csv file\n",
    "with open (election_csv) as csvfile:\n",
    "    election_csv_reader = csv.reader(csvfile)\n",
    "    header = next(election_csv_reader)\n",
    "    \n",
    "    for row in election_csv_reader:\n",
    "        totalv = totalv + 1\n",
    "        cdt = row[2]\n",
    "        if cdt in cdts: \n",
    "            cdts[cdt] += 1\n",
    "        else:\n",
    "            cdts[cdt] = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1c142ec-ebab-46fb-b93e-590a127b9092",
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate percentages and find the winner\n",
    "for cdt, votes in cdts.items():\n",
    "    pctg = (votes / totalv) * 100\n",
    "    if votes > mvotes:\n",
    "        mvotes = votes \n",
    "        winner = cdt\n",
    "    cdts[cdt] = (votes, pctg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab3357d2-9047-4f8c-8d9f-c25070f90a62",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# print results \n",
    "print(\"Election Results\")\n",
    "print(\"--------------------------\")\n",
    "print(f\"Total Votes: {totalv}\")\n",
    "print(\"--------------------------\")\n",
    "for cdt, (votes, pctg) in cdts.items():\n",
    "    print(f\"{cdt}: {pctg:.3f}% ({votes})\")\n",
    "print(\"--------------------------\")\n",
    "print(f\"Winner: {winner}\")\n",
    "print(\"--------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6b33c2c-3033-4b84-8539-558d4a0766f3",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# export results to a txt file\n",
    "ndir = 'Analysis'\n",
    "if not os.path.exists(ndir):\n",
    "    os.makedirs(ndir)\n",
    "nfile = os.path.join(ndir, 'Election Results.txt')\n",
    "\n",
    "with open (nfile, mode = 'w') as file:\n",
    "    file.write(\"Election Results\\n\")\n",
    "    file.write(\"-------------------------\\n\")\n",
    "    file.write(f\"Total Votes: {totalv}\\n\")\n",
    "    file.write(\"-------------------------\\n\")\n",
    "    for cdt, (votes, pctg) in cdts.items():\n",
    "        file.write(f\"{cdt}: {pctg:.3f}% ({votes})\\n\")\n",
    "    file.write(\"-------------------------\\n\")\n",
    "    file.write(f\"Winner: {winner}\\n\")\n",
    "    file.write(\"-------------------------\\n\")"
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
