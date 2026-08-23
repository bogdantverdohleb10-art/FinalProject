import os
import joblib
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, SearchForm
from .models import SearchHistory

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'rent_model.pkl')
model = joblib.load(MODEL_PATH)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


import os
import joblib
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, SearchForm
from .models import SearchHistory

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'rent_model.pkl')
model = joblib.load(MODEL_PATH)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def home(request):
    prediction = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            state = form.cleaned_data.get('state') or 'NY'
            beds = form.cleaned_data.get('bedrooms') or '1'
            baths = form.cleaned_data.get('bathrooms') or '1'
            sqft = form.cleaned_data.get('square_feet') or '1000'
            photo = form.cleaned_data.get('has_photo') or 'Yes'
            ptype = form.cleaned_data.get('price_type') or 'Monthly'

            lat = form.cleaned_data.get('latitude') or 38.0
            lon = form.cleaned_data.get('longitude') or -77.0

            input_data = pd.DataFrame({
                'bathrooms': [float(baths)],
                'bedrooms': [float(beds)],
                'square_feet': [int(sqft)],
                'latitude': [float(lat)],
                'longitude': [float(lon)],
                'has_photo': [photo],
                'state': [state],
                'price_type': [ptype]
            })

            exact_price = int(model.predict(input_data)[0])
            prediction = f"${exact_price}"

            query_text = f"Оплата: {ptype}, {state}, {sqft} кв.ф. Прогноз: {prediction}"
            SearchHistory.objects.create(user=request.user, query=query_text)
    else:
        form = SearchForm()

    return render(request, 'home.html', {'form': form, 'prediction': prediction})


@login_required
def history_view(request):
    history = SearchHistory.objects.filter(user=request.user).order_by('-created_at')[:15]
    return render(request, 'history.html', {'history': history})