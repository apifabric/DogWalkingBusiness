import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MaintenanceLogHomeComponent } from './home/MaintenanceLog-home.component';
import { MaintenanceLogNewComponent } from './new/MaintenanceLog-new.component';
import { MaintenanceLogDetailComponent } from './detail/MaintenanceLog-detail.component';

const routes: Routes = [
  {path: '', component: MaintenanceLogHomeComponent},
  { path: 'new', component: MaintenanceLogNewComponent },
  { path: ':id', component: MaintenanceLogDetailComponent,
    data: {
      oPermission: {
        permissionId: 'MaintenanceLog-detail-permissions'
      }
    }
  }
];

export const MAINTENANCELOG_MODULE_DECLARATIONS = [
    MaintenanceLogHomeComponent,
    MaintenanceLogNewComponent,
    MaintenanceLogDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MaintenanceLogRoutingModule { }