# Reglas ProGuard para LiberDom
# Mantener la clase MainActivity (entry point)
-keep class com.neoturcios.liberdom.MainActivity { *; }

# Mantener clases de datos usadas en serialización JSON
-keep class com.neoturcios.liberdom.MainActivity$DomainResult { *; }

# Reglas generales de Android
-keepattributes Signature
-keepattributes *Annotation*
-dontwarn javax.annotation.**
-dontwarn org.conscrypt.**
