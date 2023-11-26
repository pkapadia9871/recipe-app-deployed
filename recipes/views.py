from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Recipe                #to access Recipe model
import pandas as pd
from .forms import RecipeSearchForm
from .utils import get_name_from_id, get_chart

# Create your views here.

def recipes_home(request):
   return render(request, 'recipes/recipes_home.html')

# Create your views here.
class RecipeListView(ListView):           #class-based view
   model = Recipe                         #specify model
   template_name = 'recipes/main.html'    #specify template 

class RecipeDetailView(DetailView):                       #class-based view
   model = Recipe                                        #specify model
   template_name = 'recipes/detail.html'                 #specify template


#define function-based view - records()
def records(request):
   #create an instance of SalesSearchForm that you defined in sales/forms.py
   form = RecipeSearchForm(request.POST or None)
   sales_df=None   #initialize dataframe to None
   chart = None    #initialize chart to None
   #check if the button is clicked
   if request.method =='POST':
       #read name and chart_type
       name = request.POST.get('name')
       chart_type = request.POST.get('chart_type')

       #apply filter to extract data
       qs =Recipe.objects.filter(name=name)
       if qs:      #if data found
           #convert the queryset values to pandas dataframe
           sales_df=pd.DataFrame(qs.values()) 
           #convert the ID to Name of book
           sales_df['id']=sales_df['id'].apply(get_name_from_id)

           #call get_chart by passing chart_type from user input, sales dataframe and labels
           chart=get_chart(chart_type, sales_df)

          #convert the dataframe to HTML
           sales_df=sales_df.to_html()

   #pack up data to be sent to template in the context dictionary
   context={
           'form': form,
           'sales_df': sales_df,
           'chart': chart
           }

   #load the sales/record.html page using the data that you just prepared
   return render(request, 'recipes/records.html', context)