from .allrecipes import AllRecipes
from .budgetbytes import BudgetBytes
from .kitchn import Kitchn
from .epicurious import Epicurious
from .foodnetwork import FoodNetwork
from .saveur import Saveur
from .sirogohan import SiroGohan
from .wsonoma import WilliamsSonoma

site_classes = [AllRecipes, BudgetBytes, Epicurious, FoodNetwork, Saveur, SiroGohan, WilliamsSonoma, Kitchn]
site_urls = {}
for cls in site_classes:
    site_urls[cls.getBaseURL()] = cls
