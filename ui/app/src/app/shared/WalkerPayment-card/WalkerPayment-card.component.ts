import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WalkerPayment-card.component.html',
  styleUrls: ['./WalkerPayment-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WalkerPayment-card]': 'true'
  }
})

export class WalkerPaymentCardComponent {


}