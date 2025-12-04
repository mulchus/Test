# SOLID
# Пример с использованием SD:
# S – Принцип единственной ответственности (Single Responsibility Principle),
# O – Принцип открытости/закрытости (Open‐Closed Principle),
# L – Принцип подстановки Барбары Лисков (Liskov Substitution Principle),
# I – Принцип разделения интерфейсов (Interface Segregation Principle),
# D – Принцип инверсии зависимостей (Dependency Inversion Principle).

from abc import ABC, abstractmethod


class ReportExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass


class PDFExporter(ReportExporter):
    def export(self, data):
        print(f"Export {data} to PDF")


class ExcelExporter(ReportExporter):
    def export(self, data):
        print(f"Export {data} to Excel")


class ReportService:
    def __init__(self, exporter: ReportExporter):
        self.exporter = exporter

    def generate(self, data):
        self.exporter.export(data)


report_service = ReportService(PDFExporter())
report_service.generate("Some Data")
