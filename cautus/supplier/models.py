from django.db import models

class Entity(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em",
    )

    class Meta:
        abstract = True


class Supplier(Entity):
    corporate_name = models.CharField(
        max_length=200,
        verbose_name="Razão Social",
    )
    address = models.CharField(
        max_length=200,
        verbose_name="Endereço",
    )

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.corporate_name


class Contact(Entity):
    name = models.CharField(
        max_length=200,
        verbose_name="Nome",
    )
    email = models.CharField(
        max_length=200,
        verbose_name="E-mail",
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.DO_NOTHING,
        related_name="contacts",
        verbose_name="Fornecedor",
    )

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return self.name
