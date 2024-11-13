import frappe

@frappe.whitelist(allow_guest=True)
def get_emoji():
    frappe.only_for("System Manager")
    frappe.get_doc({"doctype": "ToDo", "description": "ToDo from api job"}).insert()
    return "🌩️"


def send_reminder_mails():
    pass

def create_todo(my_argument):
    frappe.get_doc({"doctype": "ToDo", "description": "ToDo from background job"}).insert()


# SELECT name, starts_on, type
# FROM `tabConference`
# WHERE my_conditions AND name in ("BIBAN24")
# LIMIT 20


def get_condition(user):
    frappe.errprint(user)
    return "name = 'BIBAN24'"


def has_permission(doc=None, user=None):
    if doc.name == "BIBAN24":
        frappe.throw("You don't have access to BIBAN 24")
