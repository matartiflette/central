import os
from dotenv import load_dotenv
import aspose.email as ae
from aspose.email.clients import SecurityOptions

load_dotenv()

with ae.clients.imap.ImapClient(
    os.getenv("IMAP_HOST"),
    int(os.getenv("IMAP_PORT")),
    os.getenv("IMAP_USER"),
    os.getenv("IMAP_PASSWORD")
) as client:

    client.security_options = SecurityOptions.SSLIMPLICIT
    client.select_folder("Inbox")

    for msg_info in client.list_messages():
        eml = client.fetch_message(msg_info.unique_id)