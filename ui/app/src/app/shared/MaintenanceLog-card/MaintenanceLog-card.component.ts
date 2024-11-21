import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './MaintenanceLog-card.component.html',
  styleUrls: ['./MaintenanceLog-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.MaintenanceLog-card]': 'true'
  }
})

export class MaintenanceLogCardComponent {


}