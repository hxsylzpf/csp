from django.db import models

# Create your models here.


datasets_choices = (
                ('mcdonald', 'McDonald'),
                ('tiger', 'Tiger'),
                ('shopping', 'Shopping'),
                ('brightkite', 'Brightkite'),
)
algo_choices = (
#                     ('baseline', 'Baseline'),
#                     ('naive', 'Naive'),
                ('greedy', 'Greedy'),
                )
ar_choices = (
                ('linear', 'Linear'),
                ('zipf', 'Zipf'),
                ('const', 'Constant'),
                ('step', 'Step'),
                )
budget_choices = (
                ('0.1', '0.1'),
                ('0.4', '0.4'),
                ('0.7', '0.7'),
                ('1.0', '1.0'),
                )
percent_choices = (
                ('0.1', '0.1'),
                ('0.2', '0.2'),
                ('0.3', '0.3'),
                ('0.4', '0.4'),
                ('0.5', '0.5'),
                )
mar_choices = (
                ('0.1', '0.1'),
                ('0.4', '0.4'),
                ('0.7', '0.7'),
                ('1.0', '1.0'),
                )
mtd_choices = (
                ('50', '50'),
                ('100', '100'),
                ('150', '150'),
                ('200', '200'),
                )
u_choices = (
                ('0.6', '0.6'),
                ('0.7', '0.7'),
                ('0.8', '0.8'),
                ('0.9', '0.9'),
                )
cost_choices = (
                 ('utility','utility'),
                 ('mixture','mixture'),
                 ('compactness','compactness'),
             )
bool_choices = (
                 ('true','True'),
                 ('false','False'),
             )

class Geocrowd(models.Model):
    datasets = models.CharField(max_length=10, null=False, blank=False, choices=datasets_choices)
    algos = models.CharField(max_length=10, choices=algo_choices)
    ars = models.CharField(max_length=10, choices=ar_choices)
    budgets = models.CharField(max_length=10, choices=budget_choices)
    percents = models.CharField(max_length=10, choices=percent_choices)
    mars = models.CharField(max_length=10, choices=mar_choices)
    mtds = models.CharField(max_length=10, choices=mtd_choices)
    us = models.CharField(max_length=10, choices=u_choices)
    costs = models.CharField(max_length=20, choices=cost_choices)
    subcells = models.CharField(max_length=10, choices=bool_choices)
    localness = models.CharField(max_length=10, choices=bool_choices)
    
    def __unicode__(self):
        return self.datasets
    
    