import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ClientPaymentHomeComponent } from './home/ClientPayment-home.component';
import { ClientPaymentNewComponent } from './new/ClientPayment-new.component';
import { ClientPaymentDetailComponent } from './detail/ClientPayment-detail.component';

const routes: Routes = [
  {path: '', component: ClientPaymentHomeComponent},
  { path: 'new', component: ClientPaymentNewComponent },
  { path: ':id', component: ClientPaymentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'ClientPayment-detail-permissions'
      }
    }
  }
];

export const CLIENTPAYMENT_MODULE_DECLARATIONS = [
    ClientPaymentHomeComponent,
    ClientPaymentNewComponent,
    ClientPaymentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ClientPaymentRoutingModule { }