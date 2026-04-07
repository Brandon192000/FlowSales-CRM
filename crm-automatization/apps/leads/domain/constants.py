class LeadStatus:
    NEW = "new"
    CONTACTED = "contacted"
    QUALIFIED = "qualified"
    PROPOSAL_SENT = "proposal_sent"
    WON = "won"
    LOST = "lost"

    CHOICES = [
        (NEW, "New"),
        (CONTACTED, "Contacted"),
        (QUALIFIED, "Qualified"),
        (PROPOSAL_SENT, "Proposal Sent"),
        (WON, "Won"),
        (LOST, "Lost"),
    ]


class LeadSource:
    WEBSITE = "website"
    WHATSAPP = "whatsapp"
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    REFERRAL = "referral"
    EMAIL = "email"
    OTHER = "other"

    CHOICES = [
        (WEBSITE, "Website"),
        (WHATSAPP, "WhatsApp"),
        (FACEBOOK, "Facebook"),
        (INSTAGRAM, "Instagram"),
        (REFERRAL, "Referral"),
        (EMAIL, "Email"),
        (OTHER, "Other"),
    ]