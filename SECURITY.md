## 🔒 Güvenlik Politikası

DevForge Bot, kullanıcı verilerini ve etkileşimlerini güvenli bir şekilde yönetmek için aşağıdaki güvenlik önlemlerini alır:

### 1. **Veri Koruması**
DevForge Bot, kullanıcılarla etkileşim sırasında herhangi bir kişisel veri toplamaz. Bot yalnızca gerekli API çağrıları ve komutları işler. GitHub API'si kullanılarak erişilen veriler yalnızca kullanıcıların belirttiği sorgulara dayalıdır ve botun kendisi herhangi bir kişisel bilgi saklamaz.

### 2. **Kimlik Doğrulama**
Bot, GitHub API'sine yapılan çağrılarda güvenli kimlik doğrulama sağlamak için GitHub OAuth token'ını kullanır. Bu token yalnızca bot tarafından kullanılır ve güvenli bir şekilde .env dosyasına saklanır.

### 3. **Veri Şifreleme**
Bot, Telegram API ile iletişim kurarken verilerin şifreli olarak iletilmesini sağlar. Bu sayede kullanıcı verileri Telegram sunucuları üzerinden güvenli bir şekilde iletilir.

### 4. **API Erişimi**
GitHub API erişimi yalnızca belirli, önceden tanımlanmış sorgulara dayanır. Bot, yalnızca kamuya açık verilerle çalışır. Kişisel ve gizli bilgilere erişim sağlanmaz.

### 5. **Gizlilik**
Bot, kullanıcıların kişisel bilgilerini toplamaz veya saklamaz. Telegram kullanıcı adı ve mesaj içerikleri yalnızca komutları işlemek amacıyla kullanılır ve bot sunucularında kaydedilmez.

### 6. **Güncellemeler ve Bakım**
Bot sürekli olarak güvenlik açıklarını önlemek için güncellenir. Yeni özellikler eklendikçe, güvenlik önlemleri de gözden geçirilir.

### 7. **Sorumluluk Reddi**
Bot, üçüncü tarafların hizmetlerine erişim sağladığı için, bu hizmetlerin güvenliği ve gizliliği ile ilgili hiçbir sorumluluk kabul etmez. GitHub ve Telegram API'lerinin kullanım şartları ve güvenlik politikaları, kullanıcılar tarafından kabul edilmelidir.

### 8. **Kullanıcı Uyarıları**
Herhangi bir güvenlik tehdidi veya kötüye kullanım şüphesi durumunda kullanıcılar, derhal DevForge Bot yöneticilerine bildirimde bulunmalıdır. Bot, yalnızca kullanıcıların açıkça belirtilen komutlarını işler.

