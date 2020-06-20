from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)  # выбрать количество продуктов
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput)  # скрытй параметр для управления обновление количества


class MessageSendForm(forms.Form):
    # mess_text = forms.Textarea()
    mess_text = forms.CharField(label='', max_length=200, widget=forms.Textarea(attrs={'style': 'width: 92%; '
                                                                                                'border-radius: '
                                                                                                '10px 0 0 10px; border: 1px double #858484;'}))
