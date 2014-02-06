from django.forms import ModelForm
from models import Geocrowd

class GeocrowdForm(ModelForm):
    
    class Meta:
        model = Geocrowd
        fields = ['datasets', 'algos', 'ars', 'budgets', 'percents', 'mars', 'mtds', 'us', 'costs', 'subcells', 'localness']


        labels = {
            'datasets': 'Dataset',
            'algos' : 'Algorithm',
            'ars' : 'AR function',
            'budgets' : 'Budget',
            'percents' : 'First level',
            'mars' : 'MAR',
            'mtds' : 'MTD',
            'us' : 'Utility',
            'costs' : 'Cost function',
            'subcells' : 'Sub-region',
            'localness' : 'Localness'
        }
    
    
    
#     datasets = forms.CharField(required=True, label = "Dataset", max_length=10,
#                 widget=forms.Select(choices=datasets_choices))
# 
#     algos = forms.CharField(required=True, label = "Algorithm", max_length=10,
#                 widget=forms.Select(choices=algo_choices))
#     
#     ars = forms.CharField(required=True, label = "AR function", max_length=10,
#                 widget=forms.Select(choices=ar_choices))
#     
#     budgets = forms.CharField(required=True, label = "Budget", max_length=10,
#                 widget=forms.Select(choices=budget_choices))
#             
#     mars = forms.CharField(required=True, label = "MAR", max_length=10,
#                 widget=forms.Select(choices=mar_choices))
#     
#     mtds = forms.CharField(required=True, label = "MTD", max_length=10,
#                 widget=forms.Select(choices=mtd_choices))
#     
#     us = forms.CharField(required=True, label = "Utility", max_length=10,
#                 widget=forms.Select(choices=u_choices))