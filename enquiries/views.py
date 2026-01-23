from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import EnquiryForm

def index(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()  # keep a DB record

            # Compose email with form info
            subject = f"New enquiry from {enquiry.name}"
            body = (
                f"Name: {enquiry.name}\n"
                f"Email: {enquiry.email}\n"
                f"Contact: {enquiry.contact or '-'}\n\n"
                f"Message:\n{enquiry.message}"
            )

            # Send to inbox (fallback to EMAIL_HOST_USER if DEFAULT_FROM_EMAIL missing)
            to_addr = getattr(settings, "ENQUIRIES_TO_EMAIL", None) \
                      or getattr(settings, "DEFAULT_FROM_EMAIL", None) \
                      or getattr(settings, "EMAIL_HOST_USER", None)
            if to_addr:
                EmailMessage(
                    subject=subject,
                    body=body,
                    to=[to_addr],
                    reply_to=[enquiry.email],  # allows a direct reply
                ).send(fail_silently=True)  

            return redirect("enquiries:thanks")
    else:
        form = EnquiryForm()

    return render(request, "enquiries/index.html", {"form": form})

def thanks(request):
    return render(request, "enquiries/thanks.html")
