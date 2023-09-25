from django.forms import ModelForm

from robots.models import Robot


class RobotForm(ModelForm):
    class Meta:
        model = Robot
        fields = (
            "model",
            "version",
            "created",
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.serial = f"{instance.model}-{instance.version}"

        if commit:
            instance.save()
        return instance
