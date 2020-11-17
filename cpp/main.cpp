#include <iostream>
#include <fstream>
#include <streambuf>
#include "include/jwt.h"

std::ifstream pr("../keys/fit.private.key");
std::ifstream pu("../keys/fit.public.key");

int main ( int argc, const char **argv ){

  std::string rsaPrivKey((std::istreambuf_iterator<char>(pr)),
                          std::istreambuf_iterator<char>());

  std::string rsaPublKey((std::istreambuf_iterator<char>(pu)),
                          std::istreambuf_iterator<char>());

  auto token = jwt::create()
                      .set_issuer("SSB")
                      .set_type("JWT")
                      .set_id("SsSsSsSsSB")
                      .set_issued_at(std::chrono::system_clock::now())
                      .set_expires_at(std::chrono::system_clock::now() + std::chrono::seconds{36001})
                      .set_payload_claim("sample", jwt::claim(std::string{"SSB-TEST"}))
                      .sign(jwt::algorithm::rs256(rsaPublKey, rsaPrivKey, "", ""));
  std::cout << "Your token: " << std::endl << token << std::endl;

  std::cout << std::endl;
  std::cout << "Verifing...";
  auto verify = jwt::verify()
                  .allow_algorithm(jwt::algorithm::rs256(
                      rsaPublKey, rsaPrivKey, "", ""))
                  .with_issuer("SSB");
  
  auto decoded = jwt::decode(token);
  
  verify.verify(decoded);
  std::cout << "done!" << std::endl;

  for (auto &e : decoded.get_header_claims())
    std::cout << e.first << " = " << e.second.to_json() << std::endl;
  for (auto &e : decoded.get_payload_claims())
    std::cout << e.first << " = " << e.second.to_json() << std::endl;
  return 0;
}