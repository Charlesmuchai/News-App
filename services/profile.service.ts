import { Injectable } from '@angular/core';
import { Http,Headers} from '@angular/http';
import {environment} from '../../environments/environment'
import 'rxjs/add/operator/map';

@Injectable()
export class ProfileService {

  private username:string;
  private clientid ='Iv1.64c07f667523e747';
  private clientsecret ='9b285159f984c029ac9e5ea63d917e971727456b';
  private apiKey = environment.apiKey;
  constructor(private http:Http) {
    console.log("service is now ready!");
    this.username ='Charlesmuchai';
  }
getProfileinfo(){
  return this.http.get('https://api.github.com/users/' +this.username + "?access_token=" + this.apiKey)
  .map(res => res.json());
}

getProfileRepos(){
  return this.http.get('https://api.github.com/users/' +this.username + "/repos?access_token=" + this.apiKey)
  .map(res => res.json());
}
updateProfile(username:string){
  this.username=username;
}

}
