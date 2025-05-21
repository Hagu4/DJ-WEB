from django import forms

class FeedbackForm(forms.Form):
    # Поля ввода
    name = forms.CharField(
        label="Ваше имя",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}),
        required=True
    )
    email = forms.EmailField(
        label="Ваш email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш email'}),
        required=True
    )

    # Радиокнопки (оценка сайта)
    rating = forms.ChoiceField(
        label="Оцените наш сайт",
        choices=[(1, '1 - Плохо'), (2, '2'), (3, '3'), (4, '4'), (5, '5 - Отлично')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True
    )

    # Флажки (удобство использования)
    usability = forms.MultipleChoiceField(
        label="Что вам понравилось на сайте?",
        choices=[
            ('Дизайн', 'Дизайн'),
            ('Навигация', 'Навигация'),
            ('Контент', 'Контент'),
            ('Скорость работы', 'Скорость работы'),
        ],
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False
    )

    # Выпадающий список (частота использования)
    frequency = forms.ChoiceField(
        label="Как часто вы пользуетесь нашим сайтом?",
        choices=[
            ('Ежедневно', 'Ежедневно'),
            ('Еженедельно', 'Еженедельно'),
            ('Ежемесячно', 'Ежемесячно'),
            ('Редко', 'Редко'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    # Блок ввода текста (пожелания)
    comments = forms.CharField(
        label="Ваши пожелания или комментарии",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваш комментарий'}),
        required=False
    )