from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Position, Order, Bill
from .serializers import PositionSerializers, OrderSerializers, BillSerializers
from fpdf import FPDF


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializers


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializers

    @action(detail=True)
    def generate_bill(self, request, **kwargs):
        bill = self.get_object()
        orders = bill.orders()

        txt = "Position    Amount    Price    Total    Price\n"
        for name, amount in orders.items():
            position = Position.objects.get(name=name)
            price = position.price
            txt += f"* {name} - {amount} - {price} - {amount * price}\n"
        txt += f"Total Price: {bill.total_price()}"
        self.print_bill(txt, bill.pk)

        bill.active = False
        bill.save()

        serializer = BillSerializers(bill)
        return Response(serializer.data)

    def print_bill(self, txt, pk):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_xy(0, 0)
        pdf.set_font('arial', 'B', 13.0)
        pdf.cell(ln=0, h=5.0, align='L', w=0, txt=txt, border=0)
        pdf.output(f'bill{pk}.pdf', 'F')
