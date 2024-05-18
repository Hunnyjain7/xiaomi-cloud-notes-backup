# xiaomi-cloud-notes-backup
Take the backup of notes present in the Xiaomi Phones.

* This script is answer to the below queries of user.
  * How to take the backup of all the notes present in the Xiaomi device?

# Steps to Run the script:
1. Clone the repo
    ```git clone https://github.com/Hunnyjain7/xiaomi-cloud-notes-backup```
2. Checkout main branch
    ```git checkout main```
3. Create Virtual Environment.\
    ```pip install virtualenv``` \
    ```virtualenv venv```\
    Activate Environment:\
    For Windows: ```venv\Scripts\actiavte```\
    For Linux: ```source venv/bin/activate```
4. Install Requirements ```pip install -r requirements.txt```
5. Open the `backup_notes.py`.
6. Update the `cookies` variable in the script after manually login into https://i.mi.com/ and then copy the request headers and use it here.
7. Run command: `Python backup_notes.py`
