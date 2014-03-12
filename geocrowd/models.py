from django.db import models

# Create your models here.

datasets_choices = (
                ('gowalla_LA', 'Gowalla_LA'),
                ('gowalla_SF', 'Gowalla_SF'),
                ('yelp', 'Yelp')
)
budget_choices = (
                ('1.0', '1.0'),
                ('0.7', '0.7'),
                ('0.4', '0.4'),
                ('0.1', '0.1'),
                )
percent_choices = (
                ('0.5', '0.5'),
                ('0.4', '0.4'),
                ('0.3', '0.3'),
                ('0.2', '0.2'),
                ('0.1', '0.1'),
                )
# algo_choices = (
#                 ('baseline', 'Baseline'),
#                 ('greedy', 'Greedy'),
#                 )
# ar_choices = (
#                 ('linear', 'Linear'),
#                 ('zipf', 'Zipf'),
#                 ('const', 'Constant'),
#                 ('step', 'Step'),
#                 )
# mar_choices = (
#                 ('0.1', '0.1'),
#                 ('0.4', '0.4'),
#                 ('0.7', '0.7'),
#                 ('1.0', '1.0'),
#                 )
# u_choices = (
#                 ('0.6', '0.6'),
#                 ('0.7', '0.7'),
#                 ('0.8', '0.8'),
#                 ('0.9', '0.9'),
#                 )
# heuristic_choices = (
#                  ('utility','utility'),
#                  ('hybrid','hybrid'),
#                  ('compactness','compactness'),
#              )
bool_choices = (
                 ('true','True'),
                 ('false','False'),
             )



class Geocrowd(models.Model):
    datasets = models.CharField(max_length=10, null=False, blank=False, choices=datasets_choices)
    budgets = models.CharField(max_length=10, choices=budget_choices)
    percents = models.CharField(max_length=10, choices=percent_choices)
    localness = models.CharField(max_length=10, choices=bool_choices)
        
     
#     algos = models.CharField(max_length=10, choices=algo_choices)
#     ars = models.CharField(max_length=10, choices=ar_choices)   
#     mars = models.CharField(max_length=10, choices=mar_choices)
#     us = models.CharField(max_length=10, choices=u_choices)
#     heuristics = models.CharField(max_length=20, choices=heuristic_choices)
#     subcells = models.CharField(max_length=10, choices=bool_choices)
#     constraints = models.CharField(max_length=10, choices=bool_choices)
  
    def __unicode__(self):
        return self.datasets
    
    