import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {DOGHISTORY_MODULE_DECLARATIONS, DogHistoryRoutingModule} from  './DogHistory-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    DogHistoryRoutingModule
  ],
  declarations: DOGHISTORY_MODULE_DECLARATIONS,
  exports: DOGHISTORY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class DogHistoryModule { }