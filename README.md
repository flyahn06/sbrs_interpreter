# sbrs_interpreter
사비루사어 인터프리터입니다

## 문법

### sa_bi_ru_sa
`[sa_bi_ru_sa]`

sa: 스택의 값을 1 증가합니다. <br/>
bi: 스택의 값을 1 감소합니다.<br/>
ru: 스택의 값을 프린트합니다.<br/>
saa: 현재 스택의 값을 리턴하거나, 현재 스택을 가리킵니다.<br/>

### ju_sae_no_bo
`[ju_sae_no_bo]`

ju: 스택의 값을 1 증가합니다.<br/>
sae: 스택의 값을 1 감소합니다.<br/>
no: 스택의 값을 프린트합니다.<br/>
bo: 현재 스택의 값을 리턴하거나, 현재 스택을 가리킵니다.<br/>

### sa_run_ahn_in_joe
`[sa_run_ahn_in_joe]`
sa_bi_ru_sa, ju_sae_no_bo, kkal_kkal_kki_kkol_kkal 을 모두 임포트합니다.
```
[sa_run_ahn_in_joe]
sa sa sa sa ju ju bi

sa = 3
ju = 2
```

### kkal_kkal_kki_kkol_kkal
kkal [from] [to]: from 에서 to 로 값을 옮깁니다. from 에는 null 값이 저장되며, to 에는 from 의 값이 덮어씌워집니다.
```
[sa_bi_ru_sa]
[kkal_kkal_kki_kkol_kkal]
kkal 84 saa ru

saa = 84
T
```
kki [from] [to]: to 의 값에 from 을 더한 값을 to 에 저장합니다. to의 원래 값은 무시당합니다.
```
[sa_bi_ru_sa]
[kkal_kkal_kki_kkol_kkal]
sa sa sa kki 92 saa ru

saa = 3+92 = 95
_
```
kkol: 프로그램을 종료합니다.
```
kkol

[Program Exit]
```
