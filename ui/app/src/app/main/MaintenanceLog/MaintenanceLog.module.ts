import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {MAINTENANCELOG_MODULE_DECLARATIONS, MaintenanceLogRoutingModule} from  './MaintenanceLog-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    MaintenanceLogRoutingModule
  ],
  declarations: MAINTENANCELOG_MODULE_DECLARATIONS,
  exports: MAINTENANCELOG_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class MaintenanceLogModule { }