import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './ClientPayment-card.component.html',
  styleUrls: ['./ClientPayment-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.ClientPayment-card]': 'true'
  }
})

export class ClientPaymentCardComponent {


}