from django import forms

from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model= Products
        fields=["title","desc","price","active","featured"]

    def clean_price(self):
        data=self.cleaned_data
        print("price is",self.cleaned_data)
        price=data.get("price")
        if price is not None and price<10:
           raise forms.ValidationError("price to low")
        if price is not None and price>10000:
            self.add_error("price","price too high")
        print("clean price",price)
        return price
    
    def clean(self):
        cleaned_data=self.cleaned_data
        featured=self.cleaned_data["featured"]
        active=self.cleaned_data["active"]
        data=self.cleaned_data
        price=data.get("price")
        if featured and not active:
            raise forms.ValidationError("Featured product has to be active")
        if price is not None and price<100 and featured:
            raise forms.ValidationError("Product cannot be featured")


        print("all the data",cleaned_data)
        return cleaned_data
    
    def clean_title(self):
        title=self.cleaned_data["title"]
        if not title or len(title)<3:
            raise forms.ValidationError("Title is too short or does not exists")
       

        if "free" in title:
            raise forms.ValidationError("Title contains invalid string :'free' ")
        cleaned_title=title.title().strip()
        
        return cleaned_title
    
    
    
    def clean_desc(self):
        desc=self.cleaned_data["desc"]
        if "<" in desc or ">" in desc:
            raise forms.ValidationError("Invlaid characters in desc")   
        cleaned_desc=desc.strip()
        
        return cleaned_desc

# class ProductFormOld(forms.Form):
#     title=forms.CharField()
#     desc=forms.CharField()
#     price=forms.DecimalField()
#     active=forms.BooleanField(required=False)
#     featured=forms.BooleanField(required=False)

#     def clean(self):
#         cleaned_data=self.cleaned_data
#         featured=self.cleaned_data["featured"]
#         active=self.cleaned_data["active"]
#         price=self.cleaned_data["price"]
#         if featured and not active:
#             raise forms.ValidationError("Featured product has to be active")
#         if price<100 and featured:
#             raise forms.ValidationError("Product cannot be featured")


#         print("all the data",cleaned_data)
#         return cleaned_data
    
#     def clean_title(self):
#         title=self.cleaned_data["title"]
#         if not title or len(title)<3:
#             raise forms.ValidationError("Title is too short or does not exists")
       

#         if "free" in title:
#             raise forms.ValidationError("Title contains invalid string :'free' ")
#         cleaned_title=title.title().strip()
        
#         return cleaned_title
    
#     def clean_price(self):
#         price=self.cleaned_data["price"]
#         if price<0:
#             raise forms.ValidationError("Price cannot be below 0")
#         if price>10000:
#             raise forms.ValidationError("Products is too expensive")
#         return price
    
#     def clean_desc(self):
#         desc=self.cleaned_data["desc"]
#         if "<" in desc or ">" in desc:
#             raise forms.ValidationError("Invlaid characters in desc")   
#         cleaned_desc=desc.strip()
        
#         return cleaned_desc
    


