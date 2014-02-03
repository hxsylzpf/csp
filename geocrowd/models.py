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
                ('0.4', '0.4'),
                ('0.6', '0.6'),
                ('0.8', '0.8'),
                ('1.0', '1.0'),
                )

class Geocrowd(models.Model):
    datasets = models.CharField(max_length=10, null=False, blank=False, choices=datasets_choices)
    algos = models.CharField(max_length=10, choices=algo_choices)
    ars = models.CharField(max_length=10, choices=ar_choices)
    budgets = models.CharField(max_length=10, choices=budget_choices)
    mars = models.CharField(max_length=10, choices=mar_choices)
    mtds = models.CharField(max_length=10, choices=mtd_choices)
    us = models.CharField(max_length=10, choices=u_choices)
    
    def __unicode__(self):
        return self.datasets
    
    