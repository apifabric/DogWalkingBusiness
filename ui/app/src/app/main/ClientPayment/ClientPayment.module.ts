import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CLIENTPAYMENT_MODULE_DECLARATIONS, ClientPaymentRoutingModule} from  './ClientPayment-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    ClientPaymentRoutingModule
  ],
  declarations: CLIENTPAYMENT_MODULE_DECLARATIONS,
  exports: CLIENTPAYMENT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ClientPaymentModule { }