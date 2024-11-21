import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {WALKERPAYMENT_MODULE_DECLARATIONS, WalkerPaymentRoutingModule} from  './WalkerPayment-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    WalkerPaymentRoutingModule
  ],
  declarations: WALKERPAYMENT_MODULE_DECLARATIONS,
  exports: WALKERPAYMENT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WalkerPaymentModule { }