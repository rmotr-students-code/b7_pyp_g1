class AboutView(View):
    def get(self):
        render("We're are a company that blah blah blah")

User:
    * role = regular | staff | godmode
    

class AdminView(LoginRequiretldMixin, PermissionRequiredMixin):
    required_role = 'godmode'