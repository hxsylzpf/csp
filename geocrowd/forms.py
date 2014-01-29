from django import forms

class GeocrowdForm(forms.Form):
    datasets_choices = (
                    ('mcdonald', 'McDonald'),
                    ('tiger', 'Tiger'),
    )
    algo_choices = (
                    ('baseline', 'Baseline'),
                    ('naive', 'Naive'),
                    ('greedy', 'Greedy'),
                    )
    ar_choices = (
                    ('linear', 'Linear'),
                    ('zipf', 'Zipf'),
                    )
    budget_choices = (
                    ('0', '0.1'),
                    ('1', '0.4'),
                    ('2', '0.7'),
                    ('3', '1.0'),
                    )
    mar_choices = (
                    ('0', '0.1'),
                    ('1', '0.4'),
                    ('2', '0.7'),
                    ('3', '1.0'),
                    )
    mtd_choices = (
                    ('0', '0.1'),
                    ('1', '0.4'),
                    ('2', '0.7'),
                    ('3', '1.0'),
                    )
    u_choices = (
                    ('0', '0.4'),
                    ('1', '0.6'),
                    ('2', '0.8'),
                    ('3', '1.0'),
                    )
    
    datasets = forms.CharField(required=True, label = "Dataset", max_length=10,
                widget=forms.Select(choices=datasets_choices))

    algos = forms.CharField(required=True, label = "Algorithm", max_length=10,
                widget=forms.Select(choices=algo_choices))
    
    ars = forms.CharField(required=True, label = "AR function", max_length=10,
                widget=forms.Select(choices=ar_choices))
    
    budgets = forms.CharField(required=True, label = "Budget", max_length=10,
                widget=forms.Select(choices=budget_choices))
            
    mars = forms.CharField(required=True, label = "MAR", max_length=10,
                widget=forms.Select(choices=mar_choices))
    
    mtds = forms.CharField(required=True, label = "MTD", max_length=10,
                widget=forms.Select(choices=mtd_choices))
    
    us = forms.CharField(required=True, label = "Utility", max_length=10,
                widget=forms.Select(choices=u_choices))