import frappe

def get_context(context):
    # if frappe.session.user has active subscription
    context.subscription_active = False

    context.secret_message = "Hello from riyadh.py"
