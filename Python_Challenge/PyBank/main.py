{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49bcd149-4bce-4f15-b3ce-d1ec9309eb4e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# import libraries \n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26da8f9f-4f89-4c1c-9e4e-9f51e3c8b4f5",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# open csv file\n",
    "budget_csv = os.path.join(\"Resources\",\"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e71d30e-ee42-4606-b523-ed08ec4e8d6f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# List to store data\n",
    "totalm = 0\n",
    "ntotal = 0\n",
    "prev_pr_loss = None\n",
    "change = []\n",
    "date = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42b31552-ada1-4edc-8ec2-359bc0ce0e8e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# open and read csv file\n",
    "with open (budget_csv) as csvfile:\n",
    "    budget_csv_reader = csv.reader(csvfile)\n",
    "    csv_header = next(budget_csv_reader)\n",
    "    \n",
    "# Get the total months and net total of \"Profit / Losses\"\n",
    "    for row in budget_csv_reader:\n",
    "        date_pr = row[0]\n",
    "        prof_loss = int(row[1])\n",
    "        \n",
    "        totalm = totalm + 1\n",
    "        ntotal = ntotal + prof_loss\n",
    "        \n",
    "        if prev_pr_loss is not None:\n",
    "            change_pr = prof_loss - prev_pr_loss\n",
    "            change.append(change_pr)\n",
    "            date.append(date_pr)\n",
    "        \n",
    "        prev_pr_loss = prof_loss"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90910a69-bd3d-4893-83ac-dc89faa1c10e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# average change\n",
    "if len(change) > 0:\n",
    "    avg_change = sum(change) / len(change)\n",
    "else:\n",
    "    avg_change = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "249d6e4c-af2e-40ca-ab3d-793dc945afc0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#greatest increase and decrease in profits\n",
    "if len(change) > 0:\n",
    "    grt_ic = max(change)\n",
    "    grt_dc = min(change)\n",
    "    grt_ic_dt = date[change.index(grt_ic)]\n",
    "    grt_dc_dt = date[change.index(grt_dc)]\n",
    "else:\n",
    "    grt_ic = 0\n",
    "    grt_dc = 0 \n",
    "    grt_ic_dt = ''\n",
    "    grt_dc_dt = ''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7214aa3d-5eb0-4b0c-853b-d6d607830a3a",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# print reults\n",
    "print('Financial Analysis')\n",
    "print('---------------------')\n",
    "print(f'Total Months: {totalm}')\n",
    "print(f'Total : {ntotal}')\n",
    "print(f'Average Change: $ {avg_change:.2f}')\n",
    "print(f'Greatest Increase in Profits: {grt_ic_dt} ({grt_ic})')\n",
    "print(f'Greatest Decrease in Profits: {grt_dc_dt} ({grt_dc})')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ebfcd163-0309-4cee-82f0-68935116d1f7",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# export results, to a txt file\n",
    "ndir = 'Analysis'\n",
    "if not os.path.exists(ndir):\n",
    "    os.makedirs(ndir)\n",
    "nfile = os.path.join(ndir, 'Financial Analysis.txt')\n",
    "\n",
    "with open (nfile, mode = 'w') as file:\n",
    "    file.write('Financial Analysis\\n')\n",
    "    file.write('---------------------\\n')\n",
    "    file.write(f'Total Months: {totalm}\\n')\n",
    "    file.write(f'Total : {ntotal}\\n')\n",
    "    file.write(f'Average Change: $ {avg_change:.2f}\\n')\n",
    "    file.write(f'Greatest Increase in Profits: {grt_ic_dt} ({grt_ic})\\n')\n",
    "    file.write(f'Greatest Decrease in Profits: {grt_dc_dt} ({grt_dc})\\n')\n"
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
